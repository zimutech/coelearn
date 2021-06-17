"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from cojelearningsite import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/gallery')
def gallery():
    """Renders the contact page."""
    return render_template(
        'gallery.html',
        title='Gallery',
        year=datetime.now().year,
        message='Your gallery page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/libraries')
def libraries():
    """Renders the libraries page."""
    return render_template(
        'libraries.html',
        title='Libraries',
        year=datetime.now().year,
        message='List of Libraries.'
    )

@app.route('/librariesHome')
def librariesHome():
    """Renders the libraries home page."""
    return render_template(
        'librariesHome.html',
        title='LibrariesHome',
        year=datetime.now().year,
        message='List of Libraries Home.'
    )

@app.route('/diepslootLibrary')
def diepslootLibrary():
    """Renders the Diepsloot library page."""
    return render_template(
        'region_a/diepslootLibrary.html',
        title='Diepsloot Library',
        year=datetime.now().year,
        message='Diepsloot Library page.'
    )

@app.route('/halfwayHouseLibrary')
def halfwayHouseLibrary():
    """Renders the Halfway House library page."""
    return render_template(
        'region_a/halfwayHouseLibrary.html',
        title='Halfway House Library',
        year=datetime.now().year,
        message='Halfway House Library page.'
    )

@app.route('/ivoryParkLibrary')
def ivoryParkLibrary():
    """Renders the Ivory Park library page."""
    return render_template(
        'region_a/ivoryParkLibrary.html',
        title='Ivory Park Library',
        year=datetime.now().year,
        message='Ivory Park Library page.'
    )

@app.route('/ivoryParkNorthLibrary')
def ivoryParkNorthLibrary():
    """Renders the Ivory Park North library page."""
    return render_template(
        'region_a/ivoryParkNorthLibrary.html',
        title='Ivory Park North Library',
        year=datetime.now().year,
        message='Ivory Park North Library page.'
    )

@app.route('/klipfonteinViewLibrary')
def klipfonteinViewLibrary():
    """Renders the Klipfontein View library page."""
    return render_template(
        'region_a/klipfonteinViewLibrary.html',
        title='Klipfontein View Library',
        year=datetime.now().year,
        message='klipfontein View Library page.'
    )

@app.route('/rabieRidgeLibrary')
def rabieRidgeLibrary():
    """Renders the Rabie Ridge library page."""
    return render_template(
        'region_a/rabieRidgeLibrary.html',
        title='Rabie Ridge Library',
        year=datetime.now().year,
        message='Rabie Ridge Library page.'
    )

@app.route('/blackheathLibrary')
def blackheathLibrary():
    """Renders the Blackheath library page."""
    return render_template(
        'region_b/blackheathLibrary.html',
        title='Blackheath Library',
        year=datetime.now().year,
        message='Blackheath Library page.'
    )

@app.route('/bosmontLibrary')
def bosmontLibrary():
    """Renders the Bosmont library page."""
    return render_template(
        'region_b/bosmontLibrary.html',
        title='Bosmont Library',
        year=datetime.now().year,
        message='Bosmont Library page.'
    )

@app.route('/coronationvilleLibrary')
def coronationvilleLibrary():
    """Renders the Coronationville library page."""
    return render_template(
        'region_b/coronationvilleLibrary.html',
        title='Coronationville Library',
        year=datetime.now().year,
        message='Coronationville Library page.'
    )

@app.route('/emmarentiaLibrary')
def emmarentiaLibrary():
    """Renders the Emmarentia library page."""
    return render_template(
        'region_b/emmarentiaLibrary.html',
        title='Emmarentia Library',
        year=datetime.now().year,
        message='Emmarentia Library page.'
    )

@app.route('/lindenLibrary')
def lindenLibrary():
    """Renders the Linden library page."""
    return render_template(
        'region_b/lindenLibrary.html',
        title='Linden Library',
        year=datetime.now().year,
        message='Linden Library page.'
    )

@app.route('/melvilleLibrary')
def melvilleLibrary():
    """Renders the Melville library page."""
    return render_template(
        'region_b/melvilleLibrary.html',
        title='Melville Library',
        year=datetime.now().year,
        message='Melville Library page.'
    )

@app.route('/newlandsLibrary')
def newlandsLibrary():
    """Renders the Newlands library page."""
    return render_template(
        'region_b/newlandsLibrary.html',
        title='Newlands Library',
        year=datetime.now().year,
        message='Newlands Library page.'
    )

@app.route('/parkhurstLlibrary')
def parkhurstLlibrary():
    """Renders the Parkhurst Llibrary page."""
    return render_template(
        'region_b/parkhurstLlibrary.html',
        title='ParkhurstLlibrary',
        year=datetime.now().year,
        message='Parkhurst Llibrary page.'
    )

@app.route('/parkviewLibrary')
def parkviewLibrary():
    """Renders the Parkview Library page."""
    return render_template(
        'region_b/parkviewLibrary.html',
        title='Parkview Library',
        year=datetime.now().year,
        message='Parkview Library page.'
    )

@app.route('/pennyvilleContainerLibrary')
def pennyvilleContainerLibrary():
    """Renders the Pennyville Container Library page."""
    return render_template(
        'region_b/pennyvilleContainerLibrary.html',
        title='Pennyville Container Library',
        year=datetime.now().year,
        message='Pennyville Container Library page.'
    )

@app.route('/randburgLibrary')
def randburgLibrary():
    """Renders the Randburg Library page."""
    return render_template(
        'region_b/randburgLibrary.html',
        title='Randburg Library',
        year=datetime.now().year,
        message='Randburg Library page.'
    )

@app.route('/riverleaLibrary')
def riverleaLibrary():
    """Renders the Riverlea Library page."""
    return render_template(
        'region_b/riverleaLibrary.html',
        title='Riverlea Library',
        year=datetime.now().year,
        message='Riverlea Library page.'
    )

@app.route('/rosebankLibrary')
def rosebankLibrary():
    """Renders the Rosebank Library page."""
    return render_template(
        'region_b/rosebankLibrary.html',
        title='Rosebank Library',
        year=datetime.now().year,
        message='Rosebank Library page.'
    )

@app.route('/westburyLibrary')
def westburyLibrary():
    """Renders the westburyLibrary."""
    return render_template(
        'region_b/westburyLibrary.html',
        title='Westbury Library',
        year=datetime.now().year,
        message='Westbury Library page.'
    )

@app.route('/boskruinLibrary')
def boskruinLibrary():
    """Renders the Boskruin Library page."""
    return render_template(
        'region_c/boskruinLibrary.html',
        title='Boskruin Library',
        year=datetime.now().year,
        message='Boskruin Library page.'
    )

@app.route('/braamfischervilleLibrary')
def braamfischervilleLibrary():
    """Renders the Braamfischerville Library page."""
    return render_template(
        'region_c/braamfischervilleLibrary.html',
        title='Braamfischerville Library',
        year=datetime.now().year,
        message='Braamfischerville Library page.'
    )

@app.route('/cosmoCityLibrary')
def cosmoCityLibrary():
    """Renders the Cosmo City Library page."""
    return render_template(
        'region_c/cosmoCityLibrary.html',
        title='Cosmo City Library',
        year=datetime.now().year,
        message='Cosmo City Library page.'
    )

@app.route('/davidsonvilleLibrary')
def davidsonvilleLibrary():
    """Renders the Davidsonville Library page."""
    return render_template(
        'region_c/davidsonvilleLibrary.html',
        title='Davidsonville Library',
        year=datetime.now().year,
        message='Davidsonville Library page.'
    )

@app.route('/floridaLibrary')
def floridaLibrary():
    """Renders the Florida Library page."""
    return render_template(
        'region_c/floridaLibrary.html',
        title='Florida Library',
        year=datetime.now().year,
        message='Florida Library page.'
    )

@app.route('/horizonViewLibrary')
def horizonViewLibrary():
    """Renders the Horizon View Library page."""
    return render_template(
        'region_c/horizonViewLibrary.html',
        title='Horizon View Library',
        year=datetime.now().year,
        message='Horizon View Library page.'
    )

@app.route('/leratongContainerLibrary')
def leratongContainerLibrary():
    """Renders the Leratong Container Library page."""
    return render_template(
        'region_c/leratongContainerLibrary.html',
        title='Leratong Container Library',
        year=datetime.now().year,
        message='Leratong Container Library page.'
    )

@app.route('/olivedaleLibrary')
def olivedaleLibrary():
    """Renders the Olivedale Library page."""
    return render_template(
        'region_c/olivedaleLibrary.html',
        title='Olivedale Library',
        year=datetime.now().year,
        message='Olivedale Library page.'
    )

@app.route('/roodepoortLibray')
def roodepoortLibray():
    """Renders the Roodepoort Library page."""
    return render_template(
        'region_c/roodepoortLibray.html',
        title='Roodepoort Library',
        year=datetime.now().year,
        message='Roodepoort Library page.'
    )

@app.route('/strubensvalleyLibrary')
def strubensvalleyLibrary():
    """Renders the Strubensvalley Library page."""
    return render_template(
        'region_c/strubensvalleyLibrary.html',
        title='Strubensvalley Library',
        year=datetime.now().year,
        message='Strubensvalley Library page.'
    )

@app.route('/tshepisongLibrary')
def tshepisongLibrary():
    """Renders the Tshepisong Library page."""
    return render_template(
        'region_c/tshepisongLibrary.html',
        title='Tshepisong Library',
        year=datetime.now().year,
        message='Tshepisong Library page.'
    )

@app.route('/weltevredenparkLibrary')
def weltevredenparkLibrary():
    """Renders the Weltevredenpark Library page."""
    return render_template(
        'region_c/weltevredenparkLibrary.html',
        title='Weltevredenpark Library',
        year=datetime.now().year,
        message='Weltevredenpark Library page.'
    )

@app.route('/wilroParkLibrary')
def wilroParkLibrary():
    """Renders the Wilro Park Library page."""
    return render_template(
        'region_c/wilroParkLibrary.html',
        title='Wilro Park Library',
        year=datetime.now().year,
        message='Wilro Park Library page.'
    )

@app.route('/witpoortjieLibrary')
def witpoortjieLibrary():
    """Renders the Witpoortjie Library page."""
    return render_template(
        'region_c/witpoortjieLibrary.html',
        title='Witpoortjie Library',
        year=datetime.now().year,
        message='Witpoortjie Library page.'
    )


@app.route('/diepkloofZone1Library')
def diepkloofZone1Library():
    """Renders the Diepkloof Zone 1 Library page."""
    return render_template(
        'region_d/diepkloofZone1Library.html',
        title='Diepkloof Zone 1 Library',
        year=datetime.now().year,
        message='Diepkloof Zone 1 Library page.'
    )

@app.route('/diepkloofZone5Library')
def diepkloofZone5Library():
    """Renders the Diepkloof Zone 5 Library page."""
    return render_template(
        'region_d/diepkloofZone5Library.html',
        title='Diepkloof Zone 5 Library',
        year=datetime.now().year,
        message='Diepkloof Zone 5 Library page.'
    )

@app.route('/dobsonvilleLibrary')
def dobsonvilleLibrary():
    """Renders the Dobsonville Library page."""
    return render_template(
        'region_d/dobsonvilleLibrary.html',
        title='Dobsonville Library',
        year=datetime.now().year,
        message='Dobsonville Library page.'
    )

@app.route('/emndeniLibrary')
def emndeniLibrary():
    """Renders the Emndeni Library page."""
    return render_template(
        'region_d/emndeniLibrary.html',
        title='Emndeni Library',
        year=datetime.now().year,
        message='Emndeni Library page.'
    )

@app.route('/jabavuLibrary')
def jabavuLibrary():
    """Renders the Jabavu Library page."""
    return render_template(
        'region_d/jabavuLibrary.html',
        title='Jabavu Library',
        year=datetime.now().year,
        message='Jabavu Library page.'
    )

@app.route('/klipspruitChildrensLibrary')
def klipspruitChildrensLibrary():
    """Renders the Klipspruit Childrens Library page."""
    return render_template(
        'region_d/klipspruitChildrensLibrary.html',
        title='Klipspruit Childrens Library',
        year=datetime.now().year,
        message='Klipspruit Childrens Library page.'
    )

@app.route('/klipspruitWestLibrary')
def klipspruitWestLibrary():
    """Renders the Klipspruit West Library page."""
    return render_template(
        'region_d/klipspruitWestLibrary.html',
        title='Klipspruit West Library',
        year=datetime.now().year,
        message='Klipspruit West Library page.'
    )

@app.route('/meadowlandsLibrary')
def meadowlandsLibrary():
    """Renders the Meadowlands Library page."""
    return render_template(
        'region_d/meadowlandsLibrary.html',
        title='Meadowlands Library',
        year=datetime.now().year,
        message='Meadowlands Library page.'
    )

@app.route('/mofoloLibrary')
def mofoloLibrary():
    """Renders the Mofolo Library page."""
    return render_template(
        'region_d/mofoloLibrary.html',
        title='Mofolo Library',
        year=datetime.now().year,
        message='Mofolo Library page.'
    )

@app.route('/noordgesigLibrary')
def noordgesigLibrary():
    """Renders the Noordgesig Library page."""
    return render_template(
        'region_d/noordgesigLibrary.html',
        title='Noordgesig Library',
        year=datetime.now().year,
        message='Noordgesig Library page.'
    )

@app.route('/orlandoEastLibrary')
def orlandoEastLibrary():
    """Renders the Orlando East Library page."""
    return render_template(
        'region_d/orlandoEastLibrary.html',
        title='Orlando East Library',
        year=datetime.now().year,
        message='Orlando East Library page.'
    )

@app.route('/phiriLibrary')
def phiriLibrary():
    """Renders the Phiri Library page."""
    return render_template(
        'region_d/phiriLibrary.html',
        title='Phiri Library',
        year=datetime.now().year,
        message='Phiri Library page.'
    )

@app.route('/pimvilleLibrary')
def pimvilleLibrary():
    """Renders the Pimville Library page."""
    return render_template(
        'region_d/pimvilleLibrary.html',
        title='Pimville Library',
        year=datetime.now().year,
        message='Pimville Library page.'
    )

@app.route('/proteaGlenLibrary')
def proteaGlenLibrary():
    """Renders the Protea Glen Library page."""
    return render_template(
        'region_d/proteaGlenLibrary.html',
        title='Protea Glen Library',
        year=datetime.now().year,
        message='Protea Glen Library page.'
    )

@app.route('/proteaNorthLibrary')
def proteaNorthLibrary():
    """Renders the Protea North Library page."""
    return render_template(
        'region_d/proteaNorthLibrary.html',
        title='Protea North Library',
        year=datetime.now().year,
        message='Protea North Library page.'
    )

@app.route('/slovovilleLibrary')
def slovovilleLibrary():
    """Renders the Slovoville Library page."""
    return render_template(
        'region_d/slovovilleLibrary.html',
        title='Slovoville Library',
        year=datetime.now().year,
        message='Slovoville Library page.'
    )

@app.route('/tshiaweloLibrary')
def tshiaweloLibrary():
    """Renders the Tshiawelo Library page."""
    return render_template(
        'region_d/tshiaweloLibrary.html',
        title='Tshiawelo Library',
        year=datetime.now().year,
        message='Tshiawelo Library page.'
    )

@app.route('/alexandra3rdAvenueLibrary')
def alexandra3rdAvenueLibrary():
    """Renders the Alexandra 3rd Avenue Library page."""
    return render_template(
        'region_e/alexandra3rdAvenueLibrary.html',
        title='Alexandra 3rd Avenue Library',
        year=datetime.now().year,
        message='Alexandra 3rd Avenue Library page.'
    )

@app.route('/alexandra8thAvenueLibrary')
def alexandra8thAvenueLibrary():
    """Renders the Alexandra 8th Avenue Library page."""
    return render_template(
        'region_e/alexandra8thAvenueLibrary.html',
        title='Alexandra 8th Avenue Library',
        year=datetime.now().year,
        message='Alexandra 8th Avenue Library page.'
    )

@app.route('/bryanstonLibrary')
def bryanstonLibrary():
    """Renders the Bryanston Library page."""
    return render_template(
        'region_e/bryanstonLibrary.html',
        title='Bryanston Library',
        year=datetime.now().year,
        message='Bryanston Library page.'
    )

@app.route('/killarneyLibrary')
def killarneyLibrary():
    """Renders the Killarney Library page."""
    return render_template(
        'region_e/killarneyLibrary.html',
        title='Killarney Library',
        year=datetime.now().year,
        message='Killarney Library page.'
    )

@app.route('/linbroParkLibrary')
def linbroParkLibrary():
    """Renders the Linbro Park Library page."""
    return render_template(
        'region_e/linbroParkLibrary.html',
        title='Linbro Park Library',
        year=datetime.now().year,
        message='Linbro Park Library page.'
    )

@app.route('/narscotManorLibrary')
def narscotManorLibrary():
    """Renders the Narscot Manor Library Library page."""
    return render_template(
        'region_e/narscotManorLibrary.html',
        title='Narscot Manor Library',
        year=datetime.now().year,
        message='Narscot Manor Library page.'
    )

@app.route('/orangeGroveReferenceLibrary')
def orangeGroveReferenceLibrary():
    """Renders the Orange Grove Reference Library page."""
    return render_template(
        'region_e/orangeGroveReferenceLibrary.html',
        title='Orange Grove Reference Library',
        year=datetime.now().year,
        message='Orange Grove Reference Library page.'
    )

@app.route('/riverParkLibrary')
def riverParkLibrary():
    """Renders the River Park Library page."""
    return render_template(
        'region_e/riverParkLibrary.html',
        title='River Park Library',
        year=datetime.now().year,
        message='River Park Library page.'
    )

@app.route('/rivoniaLibrary')
def rivoniaLibrary():
    """Renders the Rivonia Library page."""
    return render_template(
        'region_e/rivoniaLibrary.html',
        title='Rivonia Library',
        year=datetime.now().year,
        message='Rivonia Library page.'
    )

@app.route('/sandringhamLibrary')
def sandringhamLibrary():
    """Renders the Sandringham Library page."""
    return render_template(
        'region_e/sandringhamLibrary.html',
        title='Sandringham Library',
        year=datetime.now().year,
        message='Sandringham Library page.'
    )

@app.route('/sandtonLibrary')
def sandtonLibrary():
    """Renders the Sandton Library page."""
    return render_template(
        'region_e/sandtonLibrary.html',
        title='Sandton Library',
        year=datetime.now().year,
        message='Sandton Library page.'
    )

@app.route('/savoyLibrary')
def savoyLibrary():
    """Renders the Savoy Library page."""
    return render_template(
        'region_e/savoyLibrary.html',
        title='Savoy Library',
        year=datetime.now().year,
        message='Savoy Library page.'
    )

@app.route('/brixtonLibrary')
def brixtonLibrary():
    """Renders the Brixton Library page."""
    return render_template(
        'region_f/brixtonLibrary.html',
        title='Brixton Library',
        year=datetime.now().year,
        message='Brixton Library page.'
    )

@app.route('/glenandaLibrary')
def glenandaLibrary():
    """Renders the Glenanda Library page."""
    return render_template(
        'region_f/glenandaLibrary.html',
        title='Glenanda Library',
        year=datetime.now().year,
        message='Glenanda Library page.'
    )

@app.route('/hillbrowLibrary')
def hillbrowLibrary():
    """Renders the Hillbrow Library page."""
    return render_template(
        'region_f/hillbrowLibrary.html',
        title='Hillbrow Library',
        year=datetime.now().year,
        message='Hillbrow Library page.'
    )

@app.route('/malvernLibrary')
def malvernLibrary():
    """Renders the Malvern Library page."""
    return render_template(
        'region_f/malvernLibrary.html',
        title='Malvern Library',
        year=datetime.now().year,
        message='Malvern Library page.'
    )

@app.route('/mayfairLibrary')
def mayfairLibrary():
    """Renders the Mayfair Library page."""
    return render_template(
        'region_f/mayfairLibrary.html',
        title='Mayfair Library',
        year=datetime.now().year,
        message='Mayfair Library page.'
    )

@app.route('/murrayParkLibrary')
def murrayParkLibrary():
    """Renders the Murray Park Library page."""
    return render_template(
        'region_f/murrayParkLibrary.html',
        title='Murray Park Library',
        year=datetime.now().year,
        message='Murray Park Library page.'
    )

@app.route('/rhodesParkLibrary')
def rhodesParkLibrary():
    """Renders the Rhodes Park Library page."""
    return render_template(
        'region_f/rhodesParkLibrary.html',
        title='Rhodes Park Library',
        year=datetime.now().year,
        message='Rhodes Park Library page.'
    )

@app.route('/rossettenvilleLibrary')
def rossettenvilleLibrary():
    """Renders the Rossettenville Library page."""
    return render_template(
        'region_f/rossettenvilleLibrary.html',
        title='Rossettenville Library',
        year=datetime.now().year,
        message='Rossettenville Library page.'
    )

@app.route('/southdaleLibrary')
def southdaleLibrary():
    """Renders the Southdale Library page."""
    return render_template(
        'region_f/southdaleLibrary.html',
        title='Southdale Library',
        year=datetime.now().year,
        message='Southdale Library page.'
    )

@app.route('/southHillsLibrary')
def southHillsLibrary():
    """Renders the South Hills Library page."""
    return render_template(
        'region_f/southHillsLibrary.html',
        title='South Hills Library',
        year=datetime.now().year,
        message='South Hills Library page.'
    )

@app.route('/yeovilleLibrary')
def yeovilleLibrary():
    """Renders the Yeoville Library page."""
    return render_template(
        'region_f/yeovilleLibrary.html',
        title='Yeoville Library',
        year=datetime.now().year,
        message='Yeoville Library page.'
    )

@app.route('/drieziekLibrary')
def drieziekLibrary():
    """Renders the Drieziek Library page."""
    return render_template(
        'region_g/drieziekLibrary.html',
        title='Drieziek Library',
        year=datetime.now().year,
        message='Drieziek Library page.'
    )

@app.route('/eldoradoParkExt2Library')
def eldoradoParkExt2Library():
    """Renders the Eldorado Park Ext 2 Library page."""
    return render_template(
        'region_g/eldoradoParkExt2Library.html',
        title='Eldorado Park Ext 2 Library',
        year=datetime.now().year,
        message='Eldorado Park Ext 2 Library page.'
    )

@app.route('/eldoradoParkExt5Library')
def eldoradoParkExt5Library():
    """Renders the Drieziek Library page."""
    return render_template(
        'region_g/eldoradoParkExt5Library.html',
        title='Eldorado Park Ext 5 Library',
        year=datetime.now().year,
        message='Eldorado Park Ext 5 Library page.'
    )

@app.route('/ennerdaleExt1Library')
def ennerdaleExt1Library():
    """Renders the Ennerdale Ext 1 Library page."""
    return render_template(
        'region_g/ennerdaleExt1Library.html',
        title='Ennerdale Ext 1 Library',
        year=datetime.now().year,
        message='Ennerdale Ext 1 Library page.'
    )

@app.route('/ennerdaleExt9Library')
def ennerdaleExt9Library():
    """Renders the Ennerdale Ext 9 Library page."""
    return render_template(
        'region_g/ennerdaleExt9Library.html',
        title='Ennerdale Ext 9 Library',
        year=datetime.now().year,
        message='Ennerdale Ext 9 Library page.'
    )

@app.route('/lehaeLibrary')
def lehaeLibrary():
    """Renders the Lehae Library page."""
    return render_template(
        'region_g/lehaeLibrary.html',
        title='Lehae Library',
        year=datetime.now().year,
        message='Lehae Library page.'
    )

@app.route('/lenasiaExt1Library')
def lenasiaExt1Library():
    """Renders the Lenasia Ext 1 Library page."""
    return render_template(
        'region_g/lenasiaExt1Library.html',
        title='Lenasia Ext 1 Library',
        year=datetime.now().year,
        message='Lenasia Ext 1 Library page.'
    )

@app.route('/lenasiaExt3Library')
def lenasiaExt3Library():
    """Renders the Lenasia Ext 3 Library page."""
    return render_template(
        'region_g/lenasiaExt3Library.html',
        title='Lenasia Ext 3 Library',
        year=datetime.now().year,
        message='Lenasia Ext 3 Library page.'
    )

@app.route('/lenasiaSouthLibrary')
def lenasiaSouthLibrary():
    """Renders the Lenasia South Library page."""
    return render_template(
        'region_g/lenasiaSouthLibrary.html',
        title='Lenasia South Library',
        year=datetime.now().year,
        message='Lenasia South Library page.'
    )

@app.route('/naturenaLibrary')
def naturenaLibrary():
    """Renders the Naturena Library page."""
    return render_template(
        'region_g/naturenaLibrary.html',
        title='Naturena Library',
        year=datetime.now().year,
        message='Naturena Library page.'
    )

@app.route('/orangeFarmLibrary')
def orangeFarmLibrary():
    """Renders the Orange Farm Library page."""
    return render_template(
        'region_g/orangeFarmLibrary.html',
        title='Orange Farm Library',
        year=datetime.now().year,
        message='Orange Farm Library page.'
    )

@app.route('/poortjieLibrary')
def poortjieLibrary():
    """Renders the Poortjie Library page."""
    return render_template(
        'region_g/poortjieLibrary.html',
        title='Poortjie Library',
        year=datetime.now().year,
        message='Poortjie Library page.'
    )

@app.route('/vlakfonteinLibrary')
def vlakfonteinLibrary():
    """Renders the Vlakfontein Library page."""
    return render_template(
        'region_g/vlakfonteinLibrary.html',
        title='Vlakfontein Library',
        year=datetime.now().year,
        message='Vlakfontein Library page.'
    )

@app.route('/infoPage')
def infoPage():
    """Renders the Information page."""
    return render_template(
        'infoPage.html',
        title='Information Page',
        year=datetime.now().year,
        message='LIS Information page.'
    )

@app.route('/galleryCodingEventCodingRoadshow')
def galleryCodingEventCodingRoadshow():
    """Renders the gallery for Coding Event Coding Roadshow."""
    return render_template(
        'galleryScripts/codingEvents/codingRoadshowJabavuAndEmndeniByWETHINKcode.html',
        title='Coding Roadshow Jabavu and Emndeni',
        year=datetime.now().year,
        message='Gallery of pictures for coding event.'
    )

@app.route('/galleryCosmoCityCodingEvent')
def galleryCosmoCityCodingEvent():
    """Renders the gallery for Cosmo City Coding Event."""
    return render_template(
        'galleryScripts/codingEvents/cosmoCity.html',
        title='Coding Event For Cosmo City Coding Event',
        year=datetime.now().year,
        message='Gallery of pictures for Cosmo City Coding Event.'
    )

@app.route('/galleryEldoradoCodingEvent')
def galleryEldoradoCodingEvent():
    """Renders the gallery for Eldorado Coding Event."""
    return render_template(
        'galleryScripts/codingEvents/eldoradoCodingEvent.html',
        title='Coding Event For Eldorado Park',
        year=datetime.now().year,
        message='Gallery of pictures for Eldorado Coding Events.'
    )

@app.route('/galleryMainCodingEvent')
def galleryMainCodingEvent():
    """Renders the gallery for Main Coding Evvent."""
    return render_template(
        'galleryScripts/codingEvents/main.html',
        title='Coding Event for Main Coding Event',
        year=datetime.now().year,
        message='Gallery of pictures for Main Coding Event.'
    )

@app.route('/galleryPoortjieCodingEvent')
def galleryPoortjieCodingEvent():
    """Renders the gallery for Poortjie Coding Event."""
    return render_template(
        'galleryScripts/codingEvents/poortjie.html',
        title='Coding Event For Poortjie Coding Event',
        year=datetime.now().year,
        message='Gallery of pictures for Event For Poortjie Coding Event.'
    )

@app.route('/videoGallery')
def videoGallery():
    """Renders the video Gallery For the main video page."""
    return render_template(
        'videoGallery.html',
        title='main video gallery page',
        year=datetime.now().year,
        message='main Video gallery page.'
    )





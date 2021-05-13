def wolne_mnozenie_wielomianu(wielomian1, wielomian2):
    odp = [0.0] * (len(wielomian1) + len(wielomian2) - 1)
    for i in range(len(wielomian1)):
        for j in range(len(wielomian2)):
            odp[i + j] += wielomian1[i] * wielomian2[j]
    while len(odp) > 1 and odp[-1] == 0.0:
        odp.pop()
    return odp

def wyrownaj(wielomian1, wielomian2):
    if len(wielomian1) > len(wielomian2):
        wielomian2 = wielomian2 + [0.0] * (len(wielomian1) - len(wielomian2))
    if len(wielomian2) > len(wielomian1):
        wielomian1 = wielomian1 + [0.0] * (len(wielomian2) - len(wielomian1))
    return wielomian1, wielomian2

def dodawanie_wielomianu(wielomian1, wielomian2):
    wielomian1, wielomian2 = wyrownaj(wielomian1, wielomian2)
        
    odp = [0.0] * len(wielomian2)
    for i in range(len(wielomian1)):
        odp[i] = wielomian1[i] + wielomian2[i]
    while len(odp) > 1 and odp[-1] == 0.0:
        odp.pop()
    return odp

def odejmowanie_wielomianu(wielomian1, wielomian2):
    wielomian1, wielomian2 = wyrownaj(wielomian1, wielomian2)
        
    odp = [0.0] * len(wielomian2)
    for i in range(len(wielomian1)):
        odp[i] = wielomian1[i] - wielomian2[i]
    while len(odp) > 1 and odp[-1] == 0.0:
        odp.pop()
    return odp

def szybkie_mnozenie_wielomianu(wielomian1, wielomian2):
    wielomian1, wielomian2 = wyrownaj(wielomian1, wielomian2)
    if len(wielomian1) < 3:
        return wolne_mnozenie_wielomianu(wielomian1, wielomian2)
    k = len(wielomian1) // 2
    
    a = wielomian1[k:]
    b = wielomian1[:k]
    c = wielomian2[k:]
    d = wielomian2[:k]
    
    ac = szybkie_mnozenie_wielomianu(a, c)
    bd = szybkie_mnozenie_wielomianu(b, d)
    w = szybkie_mnozenie_wielomianu(dodawanie_wielomianu(a, b), dodawanie_wielomianu(c, d))
    w_ac_bd = odejmowanie_wielomianu(w, dodawanie_wielomianu(ac, bd))
    
    ac = [0.0] * 2 * k + ac
    w_ac_bd = [0.0] * k + w_ac_bd
    
    odp = dodawanie_wielomianu(ac, dodawanie_wielomianu(bd, w_ac_bd))
    while len(odp) > 1 and odp[-1] == 0.0:
        odp.pop()
    return odp
  

def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista

def wczytaj_rzeczywiste():
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(float(element))
    return ostateczna_lista

def wymnoz_duzo_wielomianow(wielomiany):
    if len(wielomiany) == 1:
        return wielomiany[0]
    
    k = (len(wielomiany) + 1) // 2
    lewo = wymnoz_duzo_wielomianow(wielomiany[:k])
    prawo = wymnoz_duzo_wielomianow(wielomiany[k:])
    
    return szybkie_mnozenie_wielomianu(lewo, prawo)

def rzuc_grosza_wiedzminowi_natychmiast():
    N = wczytaj_liste()[0]
    prawdopodopienstwa = wczytaj_rzeczywiste()
    rzuty = []
    for moneta in prawdopodopienstwa: 
        rzut = [1 - moneta, moneta]
        rzuty.append(rzut)
    
    po_rzutach = wymnoz_duzo_wielomianow(rzuty)
    
    odp = sum(po_rzutach[N//2+1:])
    print(odp)
    
rzuc_grosza_wiedzminowi_natychmiast()
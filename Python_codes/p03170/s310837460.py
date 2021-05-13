def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista


def kamienie_niemilosci(): 
    N, K = wczytaj_liste()
    A = wczytaj_liste()
    win = {1:'First', 2:'Second'}
    odp = []
    for i in range(K+1):
        if i < A[0]:
            odp.append(2)
        else:
            czy_istnieje = False
            for male_a in A: 
                if i - male_a >= 0 and odp[i-male_a] == 2: 
                    czy_istnieje = True
            if czy_istnieje: 
                odp.append(1)
            else: 
                odp.append(2)
    print(win[odp[K]])
    
kamienie_niemilosci()
n,l = map(int,input().split())
liste =[int(x+l) for x in range(n)]
liste2 = [abs(x) for x in liste]
roger = liste2.index(min(liste2))
liste.pop(roger)
print(sum(liste))

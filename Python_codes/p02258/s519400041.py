n = int(input())
L =[]
for i in range(n):
    x = int(input())
    L.append(x)

ma = L[1]-L[0]
mi = L[0]
for x in range(n-1):
    ma = max([ma,L[x+1]-mi])
    mi = min(mi,L[x+1])


print (ma)
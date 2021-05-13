from decimal import *

n = int(input())

a = []; b = []
ans = 0
for i in range(n):
    ai, bi = map(int,input().split())
    a.append(ai); b.append(bi)
a.sort()
b.sort()

if n % 2 == 1:
    med = (n + 1) // 2
    ans = (b[med - 1] - a[med - 1]) + 1
    print(int(ans))
else:
    med0 = n // 2
    med1 = (n // 2) + 1
    amed = (Decimal(a[med0-1])+Decimal(a[med1-1]))/Decimal(2)
    bmed = (Decimal(b[med0-1])+Decimal(b[med1-1]))/Decimal(2)
    ans = int(((bmed - amed) * Decimal(2) + Decimal(1)))
    print(ans)

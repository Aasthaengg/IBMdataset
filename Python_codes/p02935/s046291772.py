from decimal import *

N, *V = map(Decimal, open(0).read().split())
V.sort(reverse=True)

while True:
    if len(V) == 1:
        break
    x = V.pop()
    y = V.pop()
    V.append((x + y) / Decimal(2))
print(V[0])
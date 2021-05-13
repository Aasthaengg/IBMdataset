import math
from collections import Counter
a, b = map(int, input().split())
x = math.gcd(a, b)

Nso = []
Nruto = math.sqrt(x)
Nruto = math.floor(Nruto)

for i in range(2, Nruto+1):
    while x % i == 0:
        x = x//i
        Nso.append(i)
    if x == 1:
        break
    Nruto = math.sqrt(x)
    Nruto = math.floor(Nruto)

Nso.append(x)
Nso.append(1)
Nso = Counter(Nso)
print(len(Nso))

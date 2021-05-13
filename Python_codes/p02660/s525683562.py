from collections import Counter
import sys
import math
N = int(input())
M = N
Nso = []
Nruto = math.sqrt(N)
Nruto = math.ceil(Nruto)
for i in range(2, Nruto+1):
    while N % i == 0:
        N = N//i
        Nso.append(i)
    if N == 1:
        break
    Nruto = math.sqrt(N)
    Nruto = math.floor(Nruto)

Nso.append(N)
if 1 in Nso:
    Nso.remove(1)

if len(Nso) == 0:
    if M == 1:
        print(0)
    else:
        print(1)
    sys.exit()

ans = 0
Nso = Counter(Nso)

for i in Nso.values():
    x = math.sqrt(2*i)
    x = math.floor(x)
    for j in range(x, 0, -1):
        if j*j+j <= 2*i:
            ans += j
            break
print(ans)

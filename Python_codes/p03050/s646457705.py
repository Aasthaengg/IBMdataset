import math
from collections import Counter
N = int(input())
Nyakusu = []
Nruto = math.sqrt(N)
Nruto = math.ceil(Nruto)

for i in range(1, Nruto+1):
    if N % i == 0:
        Nyakusu.append(N//i-1)
        Nyakusu.append((N//(N//i))-1)
ans = 0
Nyakusu = Counter(Nyakusu)
for m in Nyakusu.keys():
    if m == 0:
        continue
    if N//m != N % m:
        continue
    ans += m
print(ans)
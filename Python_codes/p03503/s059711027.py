n = int(input())
fll = []
pll = []

for _ in range(n):
    fl = list(map(int,input().split()))
    fll.append(fl)

for _ in range(n):
    pl = list(map(int,input().split()))
    pll.append(pl)

ans = -float("inf")
from itertools import product
for bits in product([0, 1], repeat=10):
    if sum(bits) == 0:
        continue
    tmp = 0
    for fl, pl in zip(fll, pll):
        count = 0
        for f, bit in zip(fl, bits):
            if f and bit:
                count += 1
        tmp += pl[count]
    ans = max(ans, tmp)

print(ans)

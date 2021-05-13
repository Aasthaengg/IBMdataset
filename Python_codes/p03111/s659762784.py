from itertools import product
from collections import Counter as ct

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

ans = 10 ** 10
for bit in product([0, 1, 2, 3], repeat=n):
    if len(set(bit) - {0}) != 3:
        continue
    tmpa = 0
    tmpb = 0
    tmpc = 0
    for i, j in enumerate(bit):
        if j == 1:
            tmpa += l[i]
        elif j == 2:
            tmpb += l[i]
        elif j == 3:
            tmpc += l[i]
    mp = abs(a - tmpa) + abs(b - tmpb) + abs(c - tmpc)
    tmp = ct(bit)
    for i in range(1, 4):
        mp += max(0, tmp[i] - 1) * 10
    ans = min(ans, mp)
print(ans)
from itertools import permutations
from math import ceil
D = []
for _ in range(5):
    D.append(int(input()))
res = float("inf")
for a in permutations(D,5):
    t = 0
    for b in a[:-1]:
        t += ceil(b/10)*10
    t += a[-1]
    res = min(res, t)
print(res)
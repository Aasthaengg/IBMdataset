from functools import reduce
from math import ceil

n, h = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0], reverse=True)
max_a = ab[0][0]
ab = list(filter(lambda x: x[1] >= max_a, ab))

ab.sort(key=lambda x: x[1], reverse=True)
for i, v in enumerate(ab):
    h -= v[1]
    if h <= 0:
        print(i+1)
        exit()

res = ceil(h / max_a) + len(ab)
print(res)


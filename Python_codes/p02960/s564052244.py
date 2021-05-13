from collections import Counter
from itertools import product
s = list(input())
MOD = 10**9+7
c = Counter([0])
ds = list(range(10))
mods = list(range(13))

ten_power = 1
while s:
    char = s.pop()
    if char == '?':
        cand = ds
    else:
        cand = [int(char)]
    nc = Counter()
    for key, d in product(mods, cand):
        new_key = (key + d * ten_power) % 13
        nc[new_key] += c[key]
        nc[new_key] %= MOD
    c = nc
    ten_power *= 10
    ten_power %= 13

print(nc[5])
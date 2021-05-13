#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations

_, *s = open(0).read().split()
d = defaultdict(int)
for i in s:
    d[i[0]] += 1
ans = 0
for a, b, c in combinations(["M", "A", "R", "C", "H"], 3):
    ans += d[a] * d[b] * d[c]
print(ans)

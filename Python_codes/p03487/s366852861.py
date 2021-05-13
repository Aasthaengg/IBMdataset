#!/usr/bin/env python3
from collections import Counter
n, *a = map(int, open(0).read().split())
c = Counter(a)
ans = 0
for k, v in c.items():
    ans += v - k if v >= k else v
print(ans)


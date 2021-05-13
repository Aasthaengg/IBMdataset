#!/usr/bin/env python3
from collections import Counter

_, *a = map(int, open(0).read().split())
c = Counter(a)
s = sum(i * (i - 1) // 2 for i in c.values())
for i in a:
    print(s - c[i] + 1)

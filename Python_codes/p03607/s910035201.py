#!/usr/bin/env python3
from collections import defaultdict
n, *a = map(int, open(0).read().split())
b = defaultdict(int)
for i in a:
    b[i] += 1
print(sum(i % 2 > 0 for i in b.values()))

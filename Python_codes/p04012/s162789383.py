#!/usr/bin/env python3
from collections import defaultdict

w = input()
d = defaultdict(int)
for i in w:
    d[i] += 1
print("YNeos"[any(i % 2 > 0 for i in d.values())::2])

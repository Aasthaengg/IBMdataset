#!/usr/bin/env python3
from collections import Counter
input()
d = Counter(input().split())
input()
t = Counter(input().split())
for k, v in t.items():
    if k not in d or d[k] < v:
        print("NO")
        exit()
print("YES")

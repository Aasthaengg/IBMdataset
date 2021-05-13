#!/usr/bin/env python3
from collections import Counter

s = input()
ans = 100
cs = set(i for i in s)
for c in cs:
    a = 0
    ns = s
    while ns.count(c) < len(ns):
        nns = ""
        for i in range(len(ns) - 1):
            if c in (ns[i], ns[i + 1]):
                nns += c
            else:
                nns += ns[i]
        ns = nns
        a += 1
    ans = min(a, ans)
print(ans)

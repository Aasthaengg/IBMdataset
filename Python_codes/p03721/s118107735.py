#!/usr/bin/env python3
(n, k), *q = [[*map(int, i.split())] for i in open(0)]
q.sort()
for a, b in q:
    k -= b
    if k <= 0:
        print(a)
        break

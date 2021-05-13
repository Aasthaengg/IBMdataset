#!/usr/bin/env python3
(n, ), *s = [[*map(int, i.split())] for i in open(0)]
a, b = list(zip(*s))
c = 0
for i in reversed(range(n)):
    q = (a[i] + c) % b[i]
    c += b[i] - q if q > 0 else 0
print(c)

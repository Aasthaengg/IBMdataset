#!/usr/bin/env python3
(n, ), t, (m, ), *d = [[*map(int, i.split())] for i in open(0)]
s = sum(t)
for p, x in d:
    print(s - t[p - 1] + x)

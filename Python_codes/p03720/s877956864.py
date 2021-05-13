#!/usr/bin/env python3
(n, m), *r = [[*map(int, i.split())] for i in open(0)]
for i in range(1, n + 1):
    print(sum(r, []).count(i))

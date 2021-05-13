#!/usr/bin/env python3
(n, ), a, b = [[*map(int, i.split())] for i in open(0)]
print(max(sum(a[:i+1] + b[i:]) for i in range(n)))

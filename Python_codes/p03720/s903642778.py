#!/usr/bin/env python3
n, m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]

for i in range(1, n + 1):
    ac = a.count(i)
    bc = b.count(i)
    print(ac + bc)

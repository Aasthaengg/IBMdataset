#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
nn = max(a)
a.remove(nn)
nr = min(a, key=lambda x: abs(x - nn/2))
print(nn, nr)

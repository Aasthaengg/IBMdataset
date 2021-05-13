#!/usr/bin/env python3
n, *p = map(int, open(0).read().split())
b = [p[i] == i + 1 for i in range(n)]
c = 0
for i in range(1, n):
    if b[i - 1] and b[i]:
        c += 1
        b[i] = False
        b[i - 1] = False
print(c + sum(b))

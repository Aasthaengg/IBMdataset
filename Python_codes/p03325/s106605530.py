#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
c = 0
for i in a:
    b = bin(i)
    c += len(b) - 1 - b.rfind('1')
print(c)

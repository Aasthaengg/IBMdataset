#!/usr/bin/env python3
n, *h = map(int, open(0).read().split())
a = h[0]
for i in range(n-1):
    if h[i+1] - h[i] > 0:
        a += h[i+1] - h[i]
print(a)

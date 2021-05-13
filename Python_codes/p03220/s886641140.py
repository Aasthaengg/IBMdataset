#!/usr/bin/env python3
n, t, a, *h = map(int, open(0).read().split())
x = (t - a) * 1000 / 6
h = [abs(x - i) for i in h]
print(h.index(min(h)) + 1)

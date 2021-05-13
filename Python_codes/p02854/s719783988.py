#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
r = [a[0]]
for i in range(1, n):
    r.append(r[i - 1] + a[i])
print(min(abs(2 * i - r[-1]) for i in r))

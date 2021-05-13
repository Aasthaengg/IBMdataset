#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
c = 1
d = [1] * n
a = [a[0]] + [a[i] for i in range(1, n) if a[i - 1] != a[i]]
for i in range(2, len(a)):
    if (a[i] - a[i - 1]) * (a[i - 1] - a[i - 2]) < 0 and d[i - 1]:
        c += 1
        d[i] = 0
print(c)

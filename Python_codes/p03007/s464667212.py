#!/usr/bin/env python3
import bisect
n = int(input())
a = sorted(map(int, input().split()))
if n == 2:
    print(a[1] - a[0])
    print(a[1], a[0])
    exit()

p = bisect.bisect_left(a, 0)
p = min(max(1, p), n - 1)
print(sum(a[p:]) - sum(a[:p]))
b = a[p - 1]
for i in range(p, n - 1):
    print(b, a[i])
    b -= a[i]
c = a[n - 1]
for i in range(p - 1):
    print(c, a[i])
    c -= a[i]
print(c, b)

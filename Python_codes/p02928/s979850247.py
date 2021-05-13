#!/usr/bin/env python3
n, k, *a = map(int, open(0).read().split())
m = 10**9 + 7
c = [0] * 2001
t1 = [0] * n
for i in range(n):
    c[a[i]] += 1
    t1[i] = sum(c[a[i] + 1:])
t2 = [0] * n
for i in range(n):
    c[a[i]] += 1
    t2[i] = sum(c[a[i] + 1:])
s1 = sum(t1)
s2 = sum(t2)
print((s1 * k % m + k * (k - 1) // 2 * (s2 - s1) % m) % m)

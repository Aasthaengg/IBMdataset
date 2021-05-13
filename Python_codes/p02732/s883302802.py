#!/usr/bin/env python3
import collections

n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)

s = 0

for i in list(c.values()):
    s += i * (i - 1) / 2
    
for i in range(n):
    ca = c[a[i]]
    print(int(s - (ca * (ca - 1) // 2) + ((ca - 1) * (ca - 2) // 2)))

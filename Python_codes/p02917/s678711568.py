# -*- coding: utf-8 -*-

n = int(input())
b = list(map(int, input().split()))

a = [0] * (len(b) + 1)
a[0] = max(b)

for i in range(n-1):
    a[i] = min(a[i], b[i])
    a[i+1] = b[i]

print(sum(a))

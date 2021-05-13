#!/usr/bin/env python3
n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
s = sum(a)
for i in range(n):
    p = a[i]
    a[i] = max(0, a[i] - b[i])
    if a[i] == 0:
        a[i + 1] = max(0, a[i + 1] + p - b[i])

print(s - sum(a))

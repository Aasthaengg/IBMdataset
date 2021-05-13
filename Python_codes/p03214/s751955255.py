# -*- coding: utf-8 -*-
n = int(input())
a = [int(i) for i in input().split()]

average = 0
for i in range(n):
    average += a[i]
average = average / n

ans = 0
tmp = 10000
for i in range(n):
    if abs(a[i] - average) < abs(tmp - average):
        tmp = a[i]
        ans = i
print(ans)

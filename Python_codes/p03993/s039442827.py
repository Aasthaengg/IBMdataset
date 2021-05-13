#!/usr/bin/env python3

n = int(input())
a = [int(x) for x in input().split()]
c = 0
for i, ax in enumerate(a):
    if a[ax - 1] == i + 1:
        c += 1
print(c // 2)

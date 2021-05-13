#!/usr/bin/env python3

n = int(input())
a = [int(x) for x in input().split()]
c = 1
for idx, num in enumerate(a):
    if num % 2 == 0:
        c *= 2
print(3 ** len(a) - c)

#!/usr/bin/env python3
import sys
import collections

sys.setrecursionlimit(10 ** 7)

# 1 ✕ N
N, M = list(map(int, input().rstrip().split()))

# N ✕ M
A = list(tuple(map(int, input().rstrip().split())) for _ in range(M))

array = []
for x, y in A:
    array.append((y, x))

array.sort()

ans = 0
t = 0
for e, s in array:
    if t <= s:
        ans += 1
        t = e

print(ans)

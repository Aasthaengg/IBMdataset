#!/usr/bin/env python3
import sys
import collections

sys.setrecursionlimit(10 ** 7)

# 1 ✕ 1 (int)
N = int(input().rstrip())

# N ✕ M
A = list(tuple(map(int, input().rstrip().split())) for _ in range(N))

array = []
for s, t in A:
    array.append((s + t, s - t))

array.sort()
# print(array)

ans = 0
t = -1e9
for e, s in array:
    if t <= s:
        t = e
        ans += 1

print(ans)

#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

Amax = max(A)
dp = [True] * Amax
seen = set()

for a in A:
    if a in seen:
        dp[a-1] = False
        continue
    i = 2
    while i * a <= Amax:
        dp[i*a-1] = False
        i += 1
    seen.add(a)


B = [dp[a-1] for a in A]
print(sum(B))



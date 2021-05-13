#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

INF = float('inf')
abs_min = INF
neg_cnt = 0
res = 0

for i in range(N):
    if A[i] < 0:
        neg_cnt += 1
    abs_min = min(abs_min, abs(A[i]))
    res += abs(A[i])

if neg_cnt % 2:
    res -= 2 * abs_min

print(res)

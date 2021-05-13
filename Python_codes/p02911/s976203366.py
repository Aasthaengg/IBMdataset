#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, K, Q = map(int, input().split())

A = [0] * N
for i in range(Q):
    a = int(input())
    A[a-1] += 1

for i in range(N):
    if A[i] - Q + K - 1 >= 0:
        print('Yes')
    else:
        print('No')



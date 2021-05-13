#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

value = 0
for i in range(N):
    if V[i] - C[i] > 0:
        value += V[i] - C[i]

print(value)

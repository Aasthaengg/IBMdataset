#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
B = list(map(int, input().split()))

INF = float('inf')
B.append(INF)
B.insert(0, INF)

count = 0
for i in range(N):
    a = min(B[i], B[i+1])
    count += a

print(count)


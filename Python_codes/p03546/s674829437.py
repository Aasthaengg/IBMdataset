#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
edge = dict()

for i in range(10):
    edge[i] = list(map(int, input().split()))

for k in range(10):
    for i in range(10):
        for j in range(10):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

res = 0
for h in range(H):
    A = list(map(int, input().split()))
    for a in A:
        if a != -1:
            res += edge[a][1]

print(res)

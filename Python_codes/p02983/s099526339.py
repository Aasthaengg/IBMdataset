#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

L, R = map(int, input().split())


MOD = 2019

l = L % 2019
r = R % 2019

if (R//MOD) - (L//MOD) > 0:
    r += 2019

res = 2019
for i in range(l, r):
    for j in range(i+1, r+1):
        res = min((i * j) % MOD, res)

print(res)


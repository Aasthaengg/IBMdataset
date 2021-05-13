#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N, x, *A = map(int, read().split())
A = sorted(A)
cnt = 0

for a in A[:-1]:
    if x >= a:
        cnt += 1
        x -= a
if x == A[-1]:
    cnt += 1

print(cnt)

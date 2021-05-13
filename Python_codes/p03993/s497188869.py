#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

_, *A = map(int1, read().split())

ans = 0
for i, a in enumerate(A):
    if A[a] == i:
        ans += 1

print(ans // 2)

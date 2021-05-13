#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N, *A = map(int, read().split())

res = pow(3, N)
odd = 1

for a in A:
    if a % 2 == 0:
        odd *= 2

print(res - odd)

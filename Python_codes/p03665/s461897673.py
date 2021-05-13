#! /usr/bin/env python3

import sys
import numpy as np
from itertools import combinations
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N, P, *A, = map(int, read().split())

n_odd = 0
n_even = 0
for a in A:
    if a % 2 == 0:
        n_even += 1
    else:
        n_odd += 1

if n_even == N:
    if P == 0:
        print(pow(2, N))
    else:
        print(0)
else:
    print(pow(2, (N - 1)))

#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N, *A = map(int, read().split())

A = sorted(A)[::-1]
A = A[1:-N:2]

print(sum(A))

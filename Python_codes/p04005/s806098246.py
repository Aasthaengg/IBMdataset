#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

A, B, C = map(int, readline().split())

if (A % 2 == 0) or (B % 2 == 0) or (C % 2 == 0):
    print(0)
else:
    tmp = [A, B, C]
    tmp = sorted(tmp)
    print(tmp[0] * tmp[1])

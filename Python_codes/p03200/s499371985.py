#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

S = readline().decode().rstrip()

res = 0
b_cnt = 0

for c in S:
    if c == 'B':
        b_cnt += 1
    elif c == 'W':
        res += b_cnt

print(res)

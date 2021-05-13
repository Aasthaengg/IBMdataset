#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

A, B, C = map(int, read().split())

if A == B == C:
    if A % 2 == 0:
        print(-1)
    else:
        print(0)
else:
    cnt = 0
    while True:
        if (A % 2 + B % 2 + C % 2) >= 1:
            break
        cnt += 1
        A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2

    print(cnt)

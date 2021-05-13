#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)
MOD = pow(10, 9) + 7

N, C, K, *T = map(int, read().split())
T.sort()

acc = 0
n_bus = 0
cnt = 0
for t in T:
    if cnt == 0:
        acc = t + .5
        n_bus += 1
        cnt = 1
        if cnt == C:
            cnt = 0
        continue

    if t - acc <= K:
        cnt += 1
    else:
        cnt = 1
        acc = t + .5
        n_bus += 1
        continue
    if cnt == C:
        cnt = 0

print(n_bus)

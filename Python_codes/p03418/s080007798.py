#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N, K = map(int, readline().split())

if K == 0:
    print(pow(N, 2))
    sys.exit()

ans = 0
for b in range(1, N + 1):
    ans += N // b * max(0, b - K) + max(0, N % b - K + 1)

print(ans)

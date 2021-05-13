import os
import sys
from collections import Counter

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N = int(sys.stdin.buffer.readline())
A = [int(sys.stdin.buffer.readline()) for _ in range(N)]

A = np.array(A, dtype=int)
# 全部偶数になるように取れば勝てる
if np.all(A % 2 == 0):
    print('second')
else:
    print('first')

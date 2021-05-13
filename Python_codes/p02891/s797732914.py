#! /usr/bin/env python3

import sys
import numpy as np
from itertools import groupby
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

S = list(readline().decode().rstrip())
K = int(readline())

g = [len(list(g)) for _, g in groupby(S)]

if len(g) == 1:
    print(len(S) * K // 2)
else:
    acc = sum(l // 2 for l in g) * K
    if S[0] == S[-1] and g[0] % 2 == 1 and g[-1] % 2 == 1:
        acc += K - 1
    print(acc)

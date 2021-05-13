#!/usr/bin/env python3

import sys
from collections import Counter
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


N = int(input())
S = []
for i in range(N):
    s = [c for c in input()]
    s.sort()
    S.append("".join(s))

counter = Counter(S)

res = 0
for c in counter.values():
    res += c * (c-1) // 2


print(res)






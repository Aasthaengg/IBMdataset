import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = input()

ans = [0 for i in range(len(S))]

i = 0
while i < len(S):
    rc = 0
    lc = 0
    pos = 0
    while i < len(S) and S[i] != 'L':
        rc += 1
        i += 1
    pos = i
    while i < len(S) and S[i] != 'R':
        lc += 1
        i += 1
    ans[pos] += rc // 2
    ans[pos - 1] += rc // 2 + rc % 2
    ans[pos - 1] += lc // 2
    ans[pos] += lc // 2 + lc % 2

print(" ".join(map(str, ans)))
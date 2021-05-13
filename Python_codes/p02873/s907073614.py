# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
from scipy.special import comb
import copy
sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


S = S()

lis = [0] * (len(S) + 1)  # 左に連続する'<' の数、右に連続する'<'の数の大きい方
left = [0] * (len(S) + 1)
right = [0] * (len(S) + 1)
left_count = 0
for i, s in enumerate(S):
    if (s == '<'):
        left_count += 1
        left[i+1] = left_count
    else:
        left_count = 0

right_count = 0
i = len(S)
for s in reversed(S):
    if (s == '>'):
        right_count += 1
        right[i-1] = right_count
    else:
        right_count = 0
    i -= 1


ans = 0
for l, r in zip(left, right):
    ans += max(l, r)
print(ans)

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
num_w = S.count('W')
num_b = len(S) - num_w
left_w_pos = 0
ans = 0
for i, s in enumerate(S):
    if (s == 'W'):
        ans += (i-left_w_pos)
        left_w_pos += 1
print(ans)

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
# 切り上げ割り算
# -(-4 // 3)
# lis_of_lis = [[] for _ in range(N)]


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N, K = zz()
A = zz()
max_a = max(A)
rest = K
# 答えはX以下か？を考える
# 長さaの丸太を切ってX以下にするためには、
# -(-a//X)回切る必要がある


def trial(x):
    # print('try', x)
    num_cut = 0
    for a in A:
        num_cut += (-(-a//x)-1)
        # print('num_cut', num_cut)
        if (num_cut > K):
            return False
    return True


# 答えの範囲は0~max(A)
l = 0
r = max_a
while (r - l > 1):
    ans = (l + r) // 2
    if (trial(ans)):
        # print(ans)
        r = ans
    else:
        l = ans
print(r)

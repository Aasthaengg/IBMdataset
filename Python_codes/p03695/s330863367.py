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

# lis_of_lis = [[] for _ in range(N)]


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


N = z()
A = zz()
lis = list(range(-1, 3200, 400))
ok = 0
set_ = []
for i in range(N):
    if (A[i] >= 3200):
        ok += 1
    else:
        idx = bisect.bisect_left(lis, A[i])
        set_.append(idx)
set_ = set(set_)
min_ = max(len(set_), 1)
max_ = len(set_) + ok

print(min_, max_)

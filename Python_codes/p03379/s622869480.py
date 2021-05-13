# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N = z()
X = zz()
orig_X = X[:]
index = list(range(N))
# print(X, index)
X, index = zip(*sorted(zip(X, index)))

# print(X, index)
small_median = X[N//2 - 1]
big_median = X[N//2]

# print("small_median", small_median)
# print('big_median', big_median)
for i in range(N):
    if(orig_X[i] > small_median):
        pass
        print(small_median)
    else:
        pass
        print(big_median)

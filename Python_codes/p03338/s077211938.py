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


N = z()
S = S()
ans = 0
for i in range(N):
    a = collections.Counter(S[:i])
    b = collections.Counter(S[i:])
    ans = max(len(set(a.keys()) & set(b.keys())), ans)
print(ans)

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


N, K = zz()
A, B = [0]*N, [0]*N
# 力技はだめ
for i in range(N):
    A[i], B[i] = zz()
A, B = zip(*sorted(zip(A, B)))
all_num = 0
for i, b in enumerate(B):
    all_num += b
    if (all_num >= K):
        print(A[i])
        exit()

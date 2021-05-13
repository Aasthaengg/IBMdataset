# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
from collections import Counter
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


N, K = zz()
A = zz()
counter = Counter(A)
num_count = counter.most_common()
if (len(num_count) <= K):
    print(0)
    exit()

values, counts = zip(*num_count[K:])
print(sum(counts))

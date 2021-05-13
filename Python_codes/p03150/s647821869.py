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
cut_l = 0
cut_r = 0
for cut_l in range(len(S)):
    for cut_r in range(len(S)):
        # print(cut_l, cut_r)
        # print(S[:cut_l] + S[cut_r:])
        if (S[:cut_l] + S[cut_r:] == 'keyence'):
            print('YES')
            exit()
print('NO')

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
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N = z()
str_lis = ['']*N
ans_dic = defaultdict(int)
for i in range(N):
    tmp = S()
    tmp = tuple(sorted(tmp))
    ans_dic[tmp] += 1
ans = 0
for v in ans_dic.values():
    ans += comb(v, 2, exact=True)

print(ans)

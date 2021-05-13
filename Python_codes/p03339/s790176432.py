# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


def zz():
    return list(map(int, input().split()))


def z():
    return int(input())


def S():
    return input()


def C(line):
    return [input() for _ in range(line)]


N = z()
S = S()
wester = [0] * N
west_sum = 0
easter = [0] * N
sum_ = [0]*N
east_sum = S.count('E')
for i, s in enumerate(S):
    wester[i] = west_sum
    if (s == 'W'):
        west_sum += 1
    else:
        east_sum -= 1
    easter[i] = east_sum
    sum_[i] = wester[i] + easter[i]
# print(wester)
# print(easter)
print(min(sum_))

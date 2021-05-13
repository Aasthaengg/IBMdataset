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


X = z()
lis = list(range(100, 106))

max_num_item = int(X / 100)
min_num_item = int(X / 105)

for num_item in range(min_num_item, max_num_item + 1):
    tmp_x = X
    tmp_x = tmp_x - 100 * num_item
    if (tmp_x <= num_item * 5):
        print(1)
        exit()
print(0)

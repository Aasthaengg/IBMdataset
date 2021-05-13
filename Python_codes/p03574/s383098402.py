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


H, W = zz()
table = []
for i in range(H):
    table.append(input())
ans_table = [[0]*W for _ in range(H)]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
for i in range(H):
    for j in range(W):
        tmp = 0
        if (table[i][j] == '.'):
            for x, y in zip(dx, dy):
                if (i + x >= H or j+y >= W or i + x < 0 or j+y < 0):
                    continue
                if (table[i + x][j + y] == '#'):
                    tmp += 1
            ans_table[i][j] = tmp
        else:
            ans_table[i][j] = '#'


for _table in ans_table:
    print(*_table, sep='')

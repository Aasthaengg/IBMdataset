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
board = []
for i in range(H):
    board.append(S())

dx_lis = (-1, 0, 1, 0)
dy_lis = (0, -1, 0, 1)


def check(i, j):
    for dx, dy in zip(dx_lis, dy_lis):
        if (i + dx >= H or i + dx < 0 or j + dy >= W or j + dy < 0):
            continue
        if (board[i + dx][j + dy] == '#'):
            return(True)
    return False


for i in range(H):
    for j in range(W):
        if (board[i][j] == '#'):
            if (check(i, j) is False):
                print('No')
                exit()
print('Yes')

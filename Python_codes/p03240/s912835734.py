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
X, Y, H = [], [], []
Cx, Cy, Hc = 0, 0, 0
for i in range(N):
    x, y, h = zz()
    if (h != 0):
        x_t, y_t, h_t = x, y, h
    X.append(x)
    Y.append(y)
    H.append(h)
for Cx, Cy in itertools.product(range(0, 101), repeat=2):
    Hc = h_t + abs(Cx-x_t) + abs(Cy - y_t)
    # print(Cx, Cy, Hc)
    ok_count = 0
    for x, y, h in zip(X, Y, H):
        tmp = Hc - abs(Cx - x) - abs(Cy - y)
        if (h == max(tmp, 0)):
            ok_count += 1
        else:
            break
    if (ok_count == N):
        print(Cx, Cy, Hc)
        exit()

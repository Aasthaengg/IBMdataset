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


N = z()
H = zz()
H = np.array(H)
ans = 0
while (sum(H) != 0):
    s = 0
    while (s < N):
        if(H[s] != 0):
            break
        s += 1
    e = s
    while (e < N):
        if (H[e] == 0):
            break
        e += 1
    # print(H, s, ? e, '-', min(H[s:e]))
    H[s:e] -= 1
    ans += 1
print(ans)

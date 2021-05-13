# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
from itertools import accumulate
import copy


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline()[:-1] for _ in range(line)]


N = z()
ans = [0]*N
for x in range(1, 105):
    for y in range(1, 105):
        for z in range(1, 105):
            if(x**2+y**2+z**2+x*y+y*z+x*z <= N):
                ans[x**2+y**2+z**2+x*y+y*z+x*z - 1] += 1
for i in ans:
    print(i)

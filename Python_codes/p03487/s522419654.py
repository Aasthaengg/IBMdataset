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
A = zz()
dic = defaultdict(int)
for a in A:
    dic[a] += 1
ans = 0
for key in dic:
    if (dic[key] >= key):
        # kouho.append(dic[key]-key)
        ans += (dic[key]-key)
    else:
        ans += dic[key]
print(ans)

#!/usr/bin/python3
import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import unittest
from io import StringIO
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    A, B, Q = map(int, input().split())
    INF = 10**20
    s = [-INF]+[int(input()) for _ in range(A)]+[INF]
    t = [-INF]+[int(input()) for _ in range(B)]+[INF]

    for i in range(Q):
        x=int(input())
        saind = bisect.bisect_left(s,x)
        sa = s[saind-1]
        sb = s[saind]
        taind = bisect.bisect_left(t,x)
        ta = t[taind-1]
        tb = t[taind]

        res = 10**20

        for ss in (sa, sb):
            for tt in (ta, tb):
                res = min(res, abs(x-ss)+abs(ss-tt))
        
        for tt in (ta, tb):
            for ss in (sa, sb):
                res = min(res, abs(x-tt)+abs(tt-ss))


        print(res)


resolve()
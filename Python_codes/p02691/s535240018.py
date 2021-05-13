#!/usr/bin/python3
# import bisect
from collections import Counter, deque, OrderedDict,defaultdict
# from copy import copy, deepcopy
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

    N = int(input())
    A = list(map(int, input().split()))
    d=defaultdict(int)
    cnt=0
    for k,v in enumerate(A):
        d[k+v]+=1
        cnt+=d[k-v]

    print(cnt)


resolve()
#!/usr/bin/python3
import bisect
from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
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
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    s=input()

    ss=s*2
    d={}
    for k,v in enumerate(ss):
        if v in d:
            d[v].append(k)
        else: d[v]=[k]
    

    

    ls=len(s)
    t=input()
    cur=-1 #見終えた場所
    flag=False
    for i in t:
        if i in d:
            idx=d[i][bisect.bisect_left(d[i],(cur+1)%ls)]
            dif=idx-(cur+1)%ls+1
            cur+=dif
        else:
            flag=True
            break
    print(cur+1 if not flag else -1)




    
resolve()
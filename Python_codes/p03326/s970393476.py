#!/usr/bin/python3
# import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
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
    
    n,m=map(int,input().split())
    A=[list(map(int,input().split())) for i in range(n)]
    val=0
    for i in A:
        val+=sum(i)
    # bit全探索    
    # https://qiita.com/gogotealove/items/11f9e83218926211083a#%E4%BE%8B%E9%A1%8C-1
    # 昇順での探索だよ
    ans=0
    for i in range(2 ** 3):
        val=[sum(i) for i in A]

        
        """        
        10進数表記　2進数表記
        0           000
        1           001
        2           010
        3           011
        4           100
        5           101
        6           110
        7           111
        """
    
        for j in range(3):  # このループが一番のポイント
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                for k in range(n):
                    val[k]-=2*A[k][j]
        val.sort(reverse=True)
        ans=max(ans,sum(val[:m]))
    print(ans)

    

    
resolve()
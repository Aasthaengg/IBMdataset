# import bisect
from collections import Counter, deque # https://note.nkmk.me/python-scipy-connected-components/
from copy import copy, deepcopy
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
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    ans=10**4
    s=list(input())
    ss=Counter(s)
    if len(ss)==1:
        ans=0
    else:
        for k in ss.keys():
            l=copy(s)
            cnt=0

            while True:
                for i in range(len(l)-1):
                    if l[i]==k or l[i+1]==k:
                        l[i]=k
                    else:
                        continue
                l=l[:-1]
                cnt+=1
                if len(set(l))==1:
                    ans=min(ans,cnt)
                    break
    print(ans)




resolve()
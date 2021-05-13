from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# from functools import reduce
# from heapq import heapify, heappop, heappush
from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
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
    
    A=list(input())
    AA=Counter(A)

    ans=1
    alpha=list(chr(ord('a')+i) for i in range(26))
    
    for i, j in product(alpha,repeat=2):
        if i<j:
            ans+=AA[i]*AA[j]


    print(ans)


    
resolve()
# import bisect
from collections import Counter, deque # https://note.nkmk.me/python-scipy-connected-components/
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
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    S=str(input())

    SS=Counter(S)

    ans=1
    for i in SS.values():
        ans*=(i+1)
    print((ans-1)%(10**9+7))

resolve()
# import bisect
from collections import Counter, deque # https://note.nkmk.me/python-scipy-connected-components/
# from copy import copy, deepcopy
# from math import gcd
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
    S=str(input())
    SS=Counter(S).most_common()
    if len(S)==1:
        print('YES')
    if len(S)==2:
        print('YES' if len(SS)==2 else 'NO')
    if len(S)>=3:
        print('YES' if len(SS)>=3 and SS[0][1]-SS[-1][1]<=1 else 'NO')


resolve()
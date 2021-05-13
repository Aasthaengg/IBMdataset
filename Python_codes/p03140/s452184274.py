

import sys
from io import StringIO
# import bisect
from collections import Counter, deque
# from copy import copy, deepcopy
# from fractions import gcd
# from functools import reduce
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np
# from operator import xor
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline

def resolve():
    N=int(input())
    A=list(input())
    B=list(input())
    C=list(input())

    W=[[None]*3 for i in range(N)]
    for j in range(N):
        for i,k in zip([A,B,C],[0,1,2]):
            W[j][k]=i[j]

    val=0
    for k in W:
        mc=Counter(k).most_common()[0][1]
        val+=3-mc

    print(val)





resolve()
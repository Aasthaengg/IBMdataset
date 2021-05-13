import bisect,collections,copy,heapq,itertools,math,string
from collections import defaultdict as D
from functools import reduce
import numpy as np
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353    

n = I()
a = [I() for _ in range(n)]

def max_index(l, value):
    return [i for i, x in enumerate(l) if x == value]

a_sort = sorted(a,reverse=True)
# print(a_sort)

max_indexs = max_index(a,a_sort[0])
max_indexs = set(max_indexs)

for i in range(n):
    if i in max_indexs:
        print(a_sort[1])
    else:
        print(a_sort[0])

#Ap = np.array(A)
#C = np.zeros(N + 1)

# if ans:
#     print('Yes')
# else:
#     print('No')
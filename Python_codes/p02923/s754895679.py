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

N = I()
Ha = LI()

if N == 1:
    print(0)
    exit()

H = np.array(Ha,dtype='int')
# +の場合は右の要素が大きい
# 1 2 3
#   1 2 3
#   1 1
diff = H[1:]-H[:-1]
# -が連続する最大の回数をカウント
result = 0
count = 0
for i in range(N-1):
    if diff[i]<=0:
        count += 1
        continue
    else:
        result = max(count,result)
        count = 0
result = max(count,result)    

print(result)
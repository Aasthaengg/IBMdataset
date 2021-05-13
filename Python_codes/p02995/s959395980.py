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

A,B,C,D = LI()

lcm = C * D // math.gcd(C,D)

# 下側は切り上げ
# tmp = (B//C)-math.ceil(A/C)+1 + (B//D)-math.ceil(A/D)+1 - (B//lcm - math.ceil(A/lcm) + 1)
tmp = (B//C)-((A-1)//C)+1 + (B//D)-((A-1)//D)+1 - (B//lcm - ((A-1)//lcm) + 1)
# 4-2+1, 3-2+1, 1-1+1
ans = B-(A-1)+1 - tmp
print(ans)
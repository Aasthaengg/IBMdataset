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
B = LI()

A = [0]*N

A[0]=B[0]
for i in range(1,N-1):
    A[i]=min(B[i],B[i-1])
A[N-1]=B[N-2]
print(sum(A))
import bisect,collections,copy,heapq,itertools,math,string
from collections import defaultdict as D
from functools import reduce
from heapq import heappop,heappush,heapify
import numpy as np
import sys
import os
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

N, M = LI()
A = LI()

A_minus = [-x for x in A]

heapify(A_minus)

pop = lambda: -heappop(A_minus)
push = lambda x: heappush(A_minus,-x)

for _ in range(M):
    # 高速に値を取り出す。O(logN)
    x = pop()
    push(x//2)
 
answer = -sum(A_minus)
print(answer)
import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
from numba import njit
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()
Q = I()
BC = [LI() for _ in range(Q)]

sum_A = sum(A)
c = collections.Counter(A)

for pair in BC:
    num_from = pair[0]
    num_to = pair[1]
    if num_from in c:
        diff = (num_to - num_from) * c[num_from]
        sum_A += diff
        print(sum_A)
        c[num_to] += c[num_from]
        c[num_from]=0
    else:
        print(sum_A)
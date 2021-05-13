from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

A,B,K = map(int,input().split())
for i in range(K):
    if i % 2== 0:
        if A % 2 == 0:
            C = A//2
            B += C
            A -= C
        else:
            A -=1
            C = A//2
            B += C
            A -=C
    else:
        if B % 2 == 0:
            C = B//2
            B -= C
            A += C
        else:
            B -=1
            C = B//2
            A += C
            B -= C

print(A,B)
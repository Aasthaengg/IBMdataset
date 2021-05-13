"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""
import sys
input = sys.stdin.readline
from heapq import*
N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j]>A[i][k]+A[k][j]:
                print(-1)
                exit()
res = 0
for i in range(N-1):
    for j in range(i+1, N):
        for k in range(N):
            if k==i or k == j:
                continue
            if A[i][j]==A[i][k]+A[k][j]:
                break
        else:
            res += A[i][j]
print(res)

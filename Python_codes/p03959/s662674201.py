"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""

N=int(input())
T=list(map(int,input().split()))
A=list(map(int,input().split()))
mod=10**9+7
lst=[0 for i in range(N)]


lst[0]=T[0]
lst[N-1]=A[N-1]
if T[N-1]!=A[0]:
    print(0)
    exit()
for i in range(1,N):
    if T[i]>T[i-1]:
        if lst[i] and lst[i]!=T[i]:
            print(0)
            exit()
        lst[i]=T[i]

for i in range(N-2,-1,-1):
    if A[i]>A[i+1]:
        if lst[i] and lst[i]!=A[i]:
            print(0)
            exit()
        elif not lst[i] and T[i]<A[i]:
            print(0)
            exit()
        lst[i]=A[i]

count=1
for i in range(N):
    if not lst[i]:
        count=count*min(T[i],A[i])%mod
print(count)

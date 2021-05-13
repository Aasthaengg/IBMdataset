"""from collections import *
from heapq import *
from itertools import *
from fractions import gcd

from decimal import *
import copy
from bisect import *
import time"""
import sys
sys.setrecursionlimit(10**7)
input=lambda :sys.stdin.readline().rstrip()
N=int(input())
if 2<=N<=4:
    if N==2:
        print(1)
    if N==3:
        print(2)
    if N==4:
        print(2)
    exit()
count=2
visited=set()
for K in range(2,round(N**.5)+1):
    n=N
    while n%K==0:
        n//=K
    count+=n%K==1
    visited.add(K)

lst=[]
X=round(N**.5)+1
for i in range(2,round(N**.5)+1):
    if (N-1)%i==0:
        if not i in visited:
            lst.append(i)
        C=(N-1)//i
        if not C in visited:
            lst.append(C)



for K in lst:
    n=N
    while n%K==0:
        n//=K
    count+=n%K==1
    visited.add(K)
print(count)
"""
for K in C:
    n=N
    while n>=K:
        if n%K==0:
            n//=K
        else:
            n-=K
    if n==1:
        print(K,"KK")
"""

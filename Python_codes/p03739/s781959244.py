#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

ans=10**15
for t in [1,-1]:
    r=0
    cnt=0
    T=t
    for i in range(N):
        r+=A[i]
        if(T>0 and r<=0):
            cnt+=1-r
            r+=1-r
        if(T<0 and r>=0):
            cnt+=r+1
            r-=r+1
        T*=-1
    ans=min(cnt,ans)
print(ans)
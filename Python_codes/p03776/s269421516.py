import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
n,a,b=map(int,input().split())
v=list(map(int,input().split()))
v.sort(reverse=True)
ans=sum(v[:a])/a
print(ans)
res=0
r1=r2=0
def comb(n,r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

if v[a-1]==v[0]:
    for i in v:
        if i==v[0]:
            r2+=1
    for j in range(a,b+1):
        if j>r2:
            break
        res+=comb(r2,j)
    print(res)
else:   
    f=False
    first=0
    for i in range(n):
        if v[i]==v[a-1]:
            r1+=1
            if not f:
                first=i
            f=True
        elif v[i]<v[a-1]:
            break
    numa=a-first
    res+=comb(r1,numa)
    print(res)
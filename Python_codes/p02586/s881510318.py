#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect

r,c,k=map(int,input().split())
v=[[0]*c for _ in range(r)]
for i in range(k):
    ri,ci,val=map(int,input().split())
    v[ri-1][ci-1]=val
d=[[0]*(c*r) for _ in range(4)]
d[1][0]=v[0][0]
for i in range(1,c):
    d[1][i]=max(d[1][i-1],d[0][i-1]+v[0][i])
    d[2][i]=max(d[2][i-1],d[1][i-1]+v[0][i])
    d[3][i]=max(d[3][i-1],d[2][i-1]+v[0][i])
for i in range(c,r*c):
    m=0
    for j in range(4):
        m=max(m,d[j][i-c])
    cx=i%c
    rx=i//c
    d[0][i]=max(0,m)
    d[1][i]=max(d[1][i-1],m+v[rx][cx],v[rx][cx]+d[0][i-1]) if cx!=0 else max(0,v[rx][cx]+m)
    d[2][i]=max(d[2][i-1],v[rx][cx]+d[1][i-1]) if cx!=0 else 0
    d[3][i]=max(d[3][i-1],v[rx][cx]+d[2][i-1]) if cx!=0 else 0
ans=0
for j in range(4):
  ans=max(ans,d[j][r*c-1])
print(ans)
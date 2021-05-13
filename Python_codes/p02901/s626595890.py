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

n,m=map(int,input().split())
k=2**n
inf=10**7
d=[[inf]*k for _ in range(m+1)]
for i in range(m+1):
  d[i][0]=0
for i in range(m):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    res=0
    for x in c:
        res+=2**(x-1)
    for j in range(2**n):
        jx=j|res
        d[i+1][j]=min(d[i+1][j],d[i][j])
        d[i+1][jx]=min(d[i][jx],d[i][j]+a,d[i+1][jx])
if d[-1][-1]==10**7:
  print(-1)
else:
  print(d[-1][-1])

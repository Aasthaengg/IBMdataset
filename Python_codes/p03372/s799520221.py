#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n,c=map(int,input().split())
xv= [map(int, input().split()) for _ in range(n)]
x, v = [list(i) for i in zip(*xv)]
calolic=[0]*(n+1)
l=[0]*(n+1)
l[1]=v[0]
calolic[1]=max(0,l[1]-x[0])
for i in range(2,n+1):
    l[i]=l[i-1]+v[i-1]
    res=l[i]-x[i-1]
    if res>calolic[i-1]:
        calolic[i]=res
    else:
        calolic[i]=calolic[i-1]
ans=0
for i in range(n+1):
    if i==0:
        ans=max(ans,calolic[n])
    else:
        ans=max(ans,calolic[i-1]+l[-1]-l[i-1]-2*(c-x[i-1]))
calolic=[0]*(n+1)
l=[0]*(n+1)
l[1]=v[-1]
calolic[1]=max(0,l[1]-c+x[-1])
for i in range(2,n+1):
    l[i]=l[i-1]+v[n-i]
    res=l[i]-c+x[n-i]
    if res>calolic[i-1]:
        calolic[i]=res
    else:
        calolic[i]=calolic[i-1]

for i in range(n+1):
    if i==0:
        ans=max(ans,calolic[n])
    else:
        ans=max(ans,calolic[n-i]+l[-1]-l[n-i]-2*x[i-1])
print(ans)
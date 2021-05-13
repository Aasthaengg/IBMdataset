#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
h,w=map(int,input().split())
s=[input() for _ in range(h)]
l=[[0]*w for _ in range(h)]
r=[[0]*w for _ in range(h)]
u=[[0]*w for _ in range(h)]
d=[[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            l[i][j]=r[i][j]=u[i][j]=d[i][j]=0
        else: 
            l[i][j]=l[i][j-1]+1 if j!=0 else 1
            u[i][j]=u[i-1][j]+1 if i!=0 else 1
        if s[h-1-i][w-1-j]=="#":
            r[i][j]=d[i][j]=0
        else:
            r[i][j]=r[i][j-1]+1 if j!=0 else 1
            d[i][j]=d[i-1][j]+1 if i!=0 else 1
ans=0
for i in range(h):
    for j in range(w):
        res=l[i][j]+u[i][j]+r[h-1-i][w-1-j]+d[h-1-i][w-1-j]-3
        #print("##",i,j,"##",res)
        ans=max(res,ans)
print(ans)
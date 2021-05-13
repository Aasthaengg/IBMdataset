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
d=[list(map(int,input().split())) for _ in range(m)]
c_0={}
c_1={}
c_2={}

for i in range(n):
    c=list(map(int,input().split()))
    for j in range(n):
        if (i+j+2)%3==0:
            if c[j] not in c_0:
                c_0[c[j]]=1
            else:
                c_0[c[j]]+=1
        elif (i+j+2)%3==1:
            if c[j] not in c_1:
                c_1[c[j]]=1
            else:
                c_1[c[j]]+=1
        else:
            if c[j] not in c_2:
                c_2[c[j]]=1
            else:
                c_2[c[j]]+=1
color=[i for i in (range(1,m+1))]
ans=10**9
for l in itertools.permutations(color,3):
    x,y,z=l
    res=0
    for cr in c_0:
        res+=d[cr-1][x-1]*c_0[cr]
    for cr in c_1:
        res+=d[cr-1][y-1]*c_1[cr]
    for cr in c_2:
        res+=d[cr-1][z-1]*c_2[cr]
    ans=min(ans,res)
print(ans)
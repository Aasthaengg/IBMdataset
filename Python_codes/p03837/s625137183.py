#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n,m=map(int,input().split())
edge=[list(map(int,input().split())) for _ in range(m)]
           
inf=10**9
nextm=[[inf]*n for _ in range(n)]

for i in range(n):
    nextm[i][i]=0
for i in range(m):
    to,f,weight=edge[i]
    nextm[to-1][f-1]=weight
    nextm[f-1][to-1]=weight

for k in range(n):
    for i in range(n):
        for j in range(n):
            if nextm[i][j]>nextm[i][k]+nextm[k][j]:
                nextm[i][j]=nextm[i][k]+nextm[k][j]
res=0               
for i in range(m):
  a,b,c=edge[i]
  if c>nextm[a-1][b-1]:
    res+=1
print(res)
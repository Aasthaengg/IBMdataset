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
n,m=map(int,input().split())
j=0
l=[[] for _ in range(n)]
ans=[0]*m
for i in range(m):
    p,y=map(int,input().split())
    l[p-1].append((i,y,p))
for i in range(n):
    l[i].sort(key=lambda x:x[1])
for i in range(n):
    for j in range(len(l[i])):
        ans[l[i][j][0]]='%012d' %(l[i][j][2]*10**6+j+1)
print(*ans)
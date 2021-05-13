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
n,m,q=map(int,input().split())
x=[[0]*n for _ in range(n)]
for i in range(m):
    l,r=map(int,input().split())
    x[l-1][r-1]+=1
res=[[0]*n for _ in range(n)]
for i in range(n):
    res[i][0]=x[i][0]
    for j in range(1,n):
        res[i][j]=res[i][j-1]+x[i][j]
for i in range(q):
    p,q=map(int,input().split())
    ans=0
    for k in range(p-1,q):
        ans=ans+res[k][q-1]-res[k][p-2] if p!=1 else ans+res[k][q-1]
    print(ans)
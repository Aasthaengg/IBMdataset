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
b=[list(map(int,input().split())) for _ in range(n)]
res=0
ans=0
b.sort(key=lambda x: x[0])
for i in range(n):
    if res+b[i][1]<=m:
        ans+=b[i][0]*b[i][1]
        res+=b[i][1]
    else:
        ans+=b[i][0]*(m-res)
        break
print(ans)
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
d,g=map(int,input().split())
g=g//100
pc=[list(map(int,input().split())) for _ in range(d) ]
s=[0]*d
for i in range(d):
    p,c=pc[i]
    s[i]=(i+1)*p+c//100
n=2**d
ans=10**4
for i in range(0,n):
    res=0
    q=0
    for j in range(d):
        if i & (1<<j):
            res+=s[j]
            q+=pc[j][0]
    if g>res:
        q_b=q
        for j in range(d):
            if i & (1<<j):
                continue
            else:
                if (g-res)//(j+1)<pc[j][0]:
                    q_b=q+math.ceil((g-res)/(j+1))
                    ans=min(ans,q_b)
    else:
        ans=min(ans,q)
print(ans)
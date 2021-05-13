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
s=input()
n=len(s)
t=[]
x="x"
for i in range(n):
    if s[i]!=x:
        t.append([s[i],i])
m=len(t)
resl=0
resr=n-1
ans=0
for i in range((m+1)//2):
    lt,l=t[i]
    rt,r=t[m-1-i]
    if lt==rt:
        ans+=abs((l-resl)-(resr-r))
        resl=l
        resr=r
    else:
        print(-1)
        exit()
print(ans)
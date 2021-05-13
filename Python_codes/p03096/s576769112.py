##import sys
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
mod=10**9+7
n=int(input())
res=[0]*(2*10**5+1)
d=[0]*(n+1)
c_b=0
d[0]=1
for i in range(n):
    c=int(input())
    if c_b==c:
        d[i+1]=d[i]
    else:
        d[i+1]=d[i]+res[c]
        res[c]+=d[i]
        res[c]%=mod
    d[i+1]%=mod
    c_b=c
print(d[n])
#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
a.sort()
f.sort(reverse=True)
l=-1
r=a[-1]*f[0]

while r>l+1:
    cnt=0
    mid=(l+r)//2
    for i in range(n):
        cost=a[i]*f[i]
        if cost>mid:
            cnt+=a[i]-math.floor(mid/f[i])
    if cnt<=k:
        r=mid
    else:
        l=mid
print(r)
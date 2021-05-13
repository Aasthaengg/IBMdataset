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
n=int(input())
a=list(map(int,input().split()))

s=0
e=1
ans=n
acc=[0]*(n+1)
for i in range(n):
  acc[i+1]=acc[i]+a[i]
while True:
    if s==e:
      e+=1
      continue
    if s==n-1:
      
      break
    res=acc[e]-acc[s]
    for i in range(20):
        if res&(1<<i)!=0 and a[e]&(1<<i)!=0:
            s+=1
            ans+=(e-s)
            break
    else:
        e+=1
    if e==n:
      s+=1
      ans+=(e-s)
      e=n-1
print(ans)
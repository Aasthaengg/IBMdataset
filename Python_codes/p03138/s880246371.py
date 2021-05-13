#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n,k=map(int,input().split())
a=list(map(int,input().split()))
x=k.bit_length()
res=0
for i in range(x):
  c1=0
  c0=0
  for j in range(n):
    if (a[j]>>i & 1)==1:
      c1+=1
    else:
      c0+=1
  if c0>c1:
    res+=2**i
ans=0
if res>k:
  for i in range(x):
    k_res=(k>>(x-i-1))&1
    r=res>>(x-i-1)&1
    if k_res==0 and r==1:
      res-=2**(x-i-1)
    if res<=k:
      break
      
for i in range(n):
  ans+=res^a[i]
print(ans)
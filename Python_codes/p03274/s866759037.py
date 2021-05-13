import sys
#import numpy as np
#import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
n,k=map(int,input().split())
x=list(map(int,input().split()))
s=0
for i in range(n):
    if x[i]>=0:
        s=i
        break
else:
  s=n
res=10**9
if s+k-1<n:
  res=x[s+k-1]
if s-k>=0 and res>abs(x[s-k]):
  res=abs(x[s-k])
for i in range(1,k):
    if s+k-i-1>n-1 or s-i<0:
        continue
    if x[s+k-i-1]+2*abs(x[s-i])<res:
        res=x[s+k-i-1]+2*abs(x[s-i])
for i in range(1,k):
    if s-k+i<0 or s+i-1>n-1:
        continue
    if abs(x[s-k+i])+2*x[s+i-1]<res:
        res=abs(x[s-k+i])+2*x[s+i-1]
print(res)

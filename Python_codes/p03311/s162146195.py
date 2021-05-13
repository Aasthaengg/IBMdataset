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
import bisect

n=int(input())
a=list(map(int,input().split()))
c=[0]*n
for i in range(n):
    c[i]=a[i]-(i+1)
c.sort()
ans=0
if n%2==1:
  p=(n+1)//2-1
  b=c[p]
  for i in range(n):
    ans+=abs(c[i]-b)
  print(ans)
else:
  p=n//2
  b=(c[p-1]+c[p])/2
  b=round(b)
  for i in range(n):
    ans+=abs(c[i]-b)
  print(ans)
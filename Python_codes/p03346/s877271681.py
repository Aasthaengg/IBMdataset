#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
p=[int(input()) for _ in range(n)]
res=[0]*n
for i in range(n):
    res[p[i]-1]=i

k=1
x=0
if n==1:
  print(0)
  exit()
for i in range(1,n):
    if res[i-1]<res[i]:
        k+=1
    else:
        x=max(x,k)
        k=1
x=max(x,k)
print(n-x)
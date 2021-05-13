import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
input=sys.stdin.readline
h,w=map(int,input().split())
a=[list(map(str,input())) for _ in range(h)]
b=deque()
n=[-1]*(h*w)
p=((1,0),(-1,0),(0,1),(0,-1))
for x in range(h):
  for y in range(w):
    if a[x][y]=="#":
      b.append((x,y))
      n[x*w+y]=0
while b:
  x,y=b.popleft()
  for idx in p:
    s,t=idx
    if 0<=x+s<h and 0<=y+t<w:
      if n[(x+s)*w+(y+t)]==-1:
        n[(x+s)*w+(y+t)]=n[x*w+y]+1
        b.append((x+s,y+t))
print(max(n))

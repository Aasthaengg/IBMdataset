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
h,w=map(int,input().split())
s=[input() for _ in range(h)]
seen=[[0]*w for _ in range(h)]
p=[(1,0),(-1,0),(0,1),(0,-1)]
cnt=0
for i in range(h):
    cnt+=s[i].count(".")
d=deque()
d.append((0,0))
seen[0][0]=1
res=0
while True:
    if not d:
        break
    i,j=d.pop()
    for idx in p:
        x,y=idx
        if 0<=i+x<h and 0<=j+y<w and seen[i+x][j+y]==0 and s[i+x][j+y]==".":
            d.appendleft((i+x,j+y))
            seen[i+x][y+j]=seen[i][j]+1
    if seen[h-1][w-1]!=0:
        break
if seen[h-1][w-1]==0:
  print(-1)
else:
  print(cnt-seen[h-1][w-1])
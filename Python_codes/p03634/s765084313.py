#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
v=tuple(tuple(map(lambda x: int(x)-1,input().split())) for _ in range(n-1))

node=[{} for _ in range(n)]
d=deque()
ans=[None]*n
for pair in v:
    node[pair[0]][pair[1]]=pair[2]+1
    node[pair[1]][pair[0]]=pair[2]+1
q,k=map(int,input().split())
d.append(k-1)
res=[-1]*n
res[k-1]=0
while True:
    if not d:
        break
    a=d.pop()
    for x in node[a]:
        if res[x]==-1:
            res[x]=node[a][x]+res[a]
            d.append(x)
for i in range(q):
  x,y=map(int,input().split())
  print(res[x-1]+res[y-1])
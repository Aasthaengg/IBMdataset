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
#import bisect

h,w,n=map(int,input().split())
d={}
p=((1,1),(1,0),(1,-1),(0,1),(0,0),(0,-1),(-1,1),(-1,0),(-1,-1))
for i in range(n):
    a,b=map(int,input().split())
    a-=1
    b-=1
    for idx in p:
        s,t=idx
        if 0<a+s<h-1 and 0<b+t<w-1:
          if (a+s,b+t) not in d:
            d[(a+s,b+t)]=1
          else:
            d[(a+s,b+t)]+=1
ans=[0]*10
for x in d.values():
  ans[x]+=1
ans[0]=(h-2)*(w-2)-sum(ans)
print(*ans)
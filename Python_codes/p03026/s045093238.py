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
v=tuple(tuple(map(lambda x: int(x)-1,input().split())) for _ in range(n-1))
c=list(map(int,input().split()))
c.sort(reverse=True)
node=[[] for _ in range(n)]
d=deque()
d.append(0)
seen=[0]*n
seen[0]=1
ans=[0]*n
for pair in v:
    node[pair[0]].append(pair[1])
    node[pair[1]].append(pair[0])

s=0
while d:
    i=d.pop()
    ans[i]=c[s]
    s+=1
    for j in node[i]:
        if seen[j]==0:
            d.appendleft(j)
            seen[j]=1
print(sum(ans)-c[0])
print(*ans)
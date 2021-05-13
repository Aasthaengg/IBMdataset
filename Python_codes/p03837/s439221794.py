"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""
from heapq import *
N,M=map(int,input().split())
ABC=[list(map(int,input().split())) for i in range(M)]
data=[[] for i in range(N+1)]
for i,(a,b,c) in enumerate(ABC):
    data[a].append([b,c,i])
    data[b].append([a,c,i])


mlst=set()

for sp in range(1,N+1):
    visited={sp}
    dic={}
    stack=[]
    distance=[0 for i in range(N+1)]
    for p,c,i in data[sp]:
        if not c in dic:
            dic[c]=[[p,i]]
            stack.append(c)
        else:
            dic[c].append([p,i])
            stack.append(c)
    heapify(stack)
    while stack:
        m=heappop(stack)
        a,i=dic[m].pop()
        if a in visited:
            if distance[a]==m:
                mlst.add(i)
            continue
        visited.add(a)
        mlst.add(i)
        distance[a]=m
        for p,c,i in data[a]:
            if not p in visited:
                C=m+c
                heappush(stack,C)
                if C in dic:
                    dic[C].append([p,i])
                else:
                    dic[C]=[[p,i]]
print(M-len(mlst))

"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""

N,M=map(int,input().split())
LRD=[list(map(int,input().split())) for i in range(M)]

data=[[] for i in range(N+1)]
for m,(l,r,d) in enumerate(LRD):
    data[l].append([r,d,m])
    data[r].append([l,-d,m])
data2=[set([m[1] for m in data[i]]) for i in range(N+1)]
Nlst=set([i for i in range(1,N)])
Mlst=set([i for i in range(M)])
visited=set()
X=[0 for i in range(N+1)]
while Mlst:
    stack=[Nlst.pop()]
    while stack:
        l=stack.pop()
        visited.add(l)
        for r,d,m in data[l]:
            if m in Mlst:
                Mlst.remove(m)
                if not r in visited:
                    visited.add(r)
                    X[r]=X[l]+d
                    stack.append(r)

                else:
                    if X[r]!=X[l]+d:
                        print("No")
                        exit()

print("Yes")

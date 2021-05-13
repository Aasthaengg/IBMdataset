#!/usr/bin/env python3
#ABC54 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7

n,k,l = map(int,input().split())
par1 = [i for i in range(n)]
par2 = [i for i in range(n)]

rank1 = [0]*(n)
rank2 = [0]*(n)

def find(x,i):
    if i == 1:
        if par1[x] == x:
            return x
        else:
            par1[x] = find(par1[x],i)
            return par1[x]
    else:
        if par2[x] == x:
            return x
        else:
            par2[x] = find(par2[x],i)
            return par2[x]

def union(x,y,i):
    x = find(x,i)
    y = find(y,i)
    if i == 1:
        if rank1[x] < rank1[y]:
            par1[x] = y
        else:
            par1[y] = x
            if rank1[x] == rank1[y]:
                rank1[x] += 1
    else:
        if rank2[x] < rank2[y]:
            par2[x] = y
        else:
            par2[y] = x
            if rank2[x] == rank2[y]:
                rank2[x] += 1

for _ in range(k):
    p,q = map(int,input().split())
    union(p-1,q-1,1)
for _ in range(l):
    r,s = map(int,input().split())
    union(r-1,s-1,2)

f = defaultdict(lambda : 0)
for i in range(n):
    x = (find(i,1),find(i,2))
    f[x] += 1
    
ans = []
for i in range(n):
    x = (find(i,1),find(i,2))
    ans.append(f[x])
print(*ans)

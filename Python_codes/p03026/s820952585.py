import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

n=int(input())
ab=[list(map(int,input().split())) for i in range(n-1)]
c=list(map(int,input().split()))
c.sort()
print(sum(c)-c[-1])
lst=[[] for i in range(n)]
nodelst=[0]*n
ans=0
for i in range(n-1):
    a,b=ab[i]
    lst[a-1].append(b)
    lst[b-1].append(a)

# print(lst)
nodelst[0]=c[-1]
d=deque(lst[0])
cnt=-2
while d:
    tmp=d.popleft()-1
    if nodelst[tmp]==0:
        nodelst[tmp]=c[cnt]
        cnt-=1
        d+=lst[tmp]
print(*nodelst)
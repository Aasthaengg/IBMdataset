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

n,k=map(int,input().split())
td=[list(map(int,input().split())) for i in range(n)]
td.sort(key=lambda x: -x[1])

dic={}
minlst=[]
maxlst=[]
ans=0
f=0
ln=0
for i in range(n):
    t,d=td[i]
    if i<k:
        f+=d
        if not t in dic:
            dic[t]=d
        else:
            minlst.append(d)
        ln=len(dic)
    else:
        if not t in dic:
            maxlst.append(-d)
            dic[t]=d
        else:
            pass

# print(td)
# print(minlst)
# print(maxlst)
# print(f)
# print(len(dic))
# ln=len(dic)
ans=max(ans,f+pow(ln,2))
heapq.heapify(minlst)
heapq.heapify(maxlst)
while minlst and maxlst:
    f-=heapq.heappop(minlst)
    f-=heapq.heappop(maxlst)
    ln+=1
    ans=max(ans,f+pow(ln,2))
print(ans)
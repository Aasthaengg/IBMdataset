ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
import sys
gcd = math.gcd
co = collections.Counter()
n = ni()
mod=10**9+7
for i in range(n):
    a,b = ma()
    d = gcd(a,b)
    if d!=0:
        a//=d
        b//=d
    elif abs(a)>0 or abs(b)>0:
        l = max(abs(a), abs(b))
        a//=l
        b//=l
    co[(a,b)]+=1
d = collections.defaultdict(lambda:False)
ans=1
for t,cnt in co.items():
    a,b = t
    if t==(0,0) or d[t]:
        continue
    d[(a,b)]=True;d[(-a,-b)]=True;d[(b,-a)]=True;d[(-b,a)]=True
    l1 = co[(a,b)]+co[(-a,-b)]
    l2 = co[(b,-a)]+co[(-b,a)]
    ans=ans*(pow(2,l1,mod)+pow(2,l2,mod) -1)%mod
    ans%=mod
print((ans-1 +co[(0,0)])%mod)

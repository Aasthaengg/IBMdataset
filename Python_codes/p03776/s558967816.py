#!/usr/bin/env python3
INF=1e10

def comb(a, b):
    res=1
    for i in range(b):
        res*=(a-i)
    for i in range(b):
        res//=(b-i)
    return res

from collections import defaultdict
N,A,B=map(int, input().split())
V=list(map(int, input().split()))
V=sorted(V, reverse=True)
cnts = defaultdict(lambda: 0)
for v in V:
    cnts[v]+=1

ans, cnt = -INF, 0
for n in range(A, B+1):
    tmp = sum(V[:n])/n
    if tmp < ans:
        continue
    if tmp > ans:
        ans=tmp
        cnt=0
    nb = 0
    for i in range(n):
        if V[i]==V[n-1]:
            nb+=1
    cnt += comb(cnts[V[n-1]], nb)
print(ans)
print(cnt)
        

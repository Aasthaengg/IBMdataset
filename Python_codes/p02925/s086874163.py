#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
A=[list(map(int,input().split())) for i in range(n)]
now=[0]*n
rest=n*(n-1)//2
for i in range(n):
    for j in range(n-1):
        A[i][j]=A[i][j]-1

S={i for i in range(n)}
tmp=set()
while rest and S:
    used=[0]*n  
    # print(now)
    count+=1
    for si in S:
        if n-1<=now[si]:
            continue
        ene=A[si][now[si]]
        if n-1<=now[ene]:
            continue
        if A[ene][now[ene]] == si and not(used[si] or used[ene]):
            rest-=1
            now[si]+=1; now[ene]+=1
            used[si]=used[ene]=1
            tmp.add(si); tmp.add(ene)
    S=tmp.copy(); tmp=set()
for ni in now:
    if ni != n-1:
        print(-1)
        break
else:
    print(count)




# coding: utf-8
from heapq import heappop, heappush
from itertools import permutations
N,M,R=map(int,input().split())
r_list=list(map(int,input().split()))

INF=10**11
G=[[INF for j in range(N+1)] for i in range(N+1)]
conection=[[] for i in range(N+1)]

RG=[[INF for j in range(N+1)] for i in range(N+1)]

for i in range(M):
    A,B,C=map(int,input().split())
    G[A][B]=C
    G[B][A]=C
    conection[A].append(B)
    conection[B].append(A)

for k in range(R):
    start=r_list[k]
    d=[INF for i in range(N+1)]
    d[start]=0
    
    used=[False for i in range(N+1)]
    
    heap=[]
    heappush(heap,(d[start],start))
    
    while heap:
        d_u, u = heappop(heap)
        used[u] = True

        if d[u] < d_u:
            continue
        
        for v in conection[u]:
            if not(used[v]) and d_u + G[u][v] < d[v]:
                d[v] = d_u + G[u][v]
                heappush(heap,(d[v],v))
    
    for i in range(R):
        r=r_list[i]
        RG[start][r]=d[r]
        RG[r][start]=d[r]
        
P=permutations(r_list,R)
ans=INF

for p in P:
    tmp=0
    for j in range(R-1):
        tmp+=RG[p[j]][p[j+1]]
    ans=min(ans,tmp)

print(ans)
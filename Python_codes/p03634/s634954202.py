# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    edge=[[] for _ in range(N)]
    for _ in range(N-1):
        a,b,c=map(int1,input().split())
        c+=1
        edge[a].append((c,b))
        edge[b].append((c,a))
    
    Q,K=map(int,input().split())
    K-=1
    from heapq import heappop,heappush
    def dijkstra(start,n,edges):
        d=[INF]*n
        used=[False]*n
        d[start]=0
        used[start]=True
        edgelist=[]
        for edge in edges[start]:
            heappush(edgelist,edge)
        while edgelist:
            minedge=heappop(edgelist)
            if used[minedge[1]]:
                continue
            v=minedge[1]
            d[v]=minedge[0]
            used[v]=True
            for edge in edges[v]:
                if not used[edge[1]]:
                    heappush(edgelist,(edge[0]+d[v],edge[1]))
        return d
    
    d=dijkstra(K,N,edge)
    for _ in range(Q):
        x,y=map(int1,input().split())
        print(d[x]+d[y])

if __name__ == '__main__':
    main()

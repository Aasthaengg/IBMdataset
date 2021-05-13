N,M=map(int, input().split())
E=[[] for _ in range(N)]
for i in range(M):
    a,b,c=map(int, input().split())
    E[a-1].append((b-1,c,i))
    E[b-1].append((a-1,c,i))

ans=[1]*M

import heapq
def dijkstra(s):
    distance=[-1]*N
    parent_n=[-1]*N
    parent_e=[-1]*N
    distance[s]=0
    parent_n[s]=s
    q=[(0,s)]
    while q:
        nc,n=heapq.heappop(q)
        for to,c,eid in E[n]:
            if distance[to]<0 or nc+c<distance[to]:
                distance[to]=nc+c
                parent_n[to]=n
                parent_e[to]=eid
                heapq.heappush(q,(nc+c,to))
    checked=[False]*N
    checked[s]=True
    for i in range(N):
        if checked[i]: continue
        n=i
        while n!=s:
            checked[n]=True
            ans[parent_e[n]]=0
            n=parent_n[n]

for i in range(N): dijkstra(i)
print(sum(ans))
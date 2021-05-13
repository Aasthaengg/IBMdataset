from collections import deque

N,M=map(int,input().split())
G=[[] for i in range(N)]
for i in range(M):
    L,R,D=map(int,input().split())
    L,R=L-1,R-1
    G[L].append((D,R))
    G[R].append((-D,L))
ok=True
dist=[None]*N
que=deque()
for i in range(N):
    if dist[i]!=None:
        continue
    que.append(i)
    dist[i]=0
    while que:
        v=que.popleft()
        for cost,nv in G[v]:
            if dist[nv]!=None:
                if dist[nv]!=dist[v]+cost:
                    print('No')
                    exit()
            else:
                dist[nv]=dist[v]+cost
                que.append(nv)

print('Yes')
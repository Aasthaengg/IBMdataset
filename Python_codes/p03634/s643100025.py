from collections import deque

N=int(input())
g=[[] for _ in range(N)]
visit=[0]*N
dist=[0]*N

for _ in range(N-1):
    a,b,c=list(map(int,input().split()))
    a-=1
    b-=1

    g[a].append([b,c])
    g[b].append([a,c])


Q,K=list(map(int,input().split()))
K-=1

q=deque([K])
visit[K]=1

while len(q)>0:
    p=q.popleft()
    
    for c,d in g[p]:
        if visit[c]==0:
            dist[c]=d+dist[p]
            visit[c]=1
            q.append(c)
    
for _ in range(Q):
    x,y=list(map(int,input().split()))
    x-=1
    y-=1
    print(dist[x]+dist[y])
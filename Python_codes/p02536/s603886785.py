from collections import deque
n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)
visited=[0]*n
def bfs(s):
    q=deque([s])
    visited[s]=1
    while q:
        x=q.popleft()
        for nx in edge[x]:
            if visited[nx]==0:
                visited[nx]=1
                q.append(nx)
    return
ans=0
for s in range(n):
    if visited[s]==0:
        bfs(s)
        ans+=1
print(ans-1)
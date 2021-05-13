from collections import deque
n=int(input())
edge=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)
def bfs(s):
    visited=[-1]*n
    q=deque([s])
    visited[s]=0
    while q:
        x=q.popleft()
        for nx in edge[x]:
            if visited[nx]==-1:
                visited[nx]=visited[x]+1
                q.append(nx)
    return visited
visited1=bfs(0)
visitedn=bfs(n-1)
dist=visited1[n-1]-1
if dist%2:
    for i in range(n):
        if visited1[i]==-(-dist//2) and visitedn[i]==-(-dist//2):
            a=i
        if visited1[i]==-(-dist//2)+1 and visitedn[i]==-(-dist//2)-1:
            b=i
else:
    for i in range(n):
        if visited1[i]==-(-dist//2) and visitedn[i]==-(-dist//2)+1:
            a=i
        if visitedn[i]==-(-dist//2) and visited1[i]==-(-dist//2)+1:
            b=i
edge[a].remove(b)
edge[b].remove(a)
visited=[0]*n
q=deque([0])
visited[0]=1
while q:
    x=q.popleft()
    for nx in edge[x]:
        if visited[nx]==0:
            visited[nx]=1
            q.append(nx)
fs=sum(visited)+(-dist//2)-1
ss=n-sum(visited)-dist//2-1
if dist%2:
    if fs>=ss:
        print("Fennec")
    else:
        print("Snuke")
else:
    if fs>ss:
        print("Fennec")
    else:
        print("Snuke")
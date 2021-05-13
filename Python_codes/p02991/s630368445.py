from collections import deque
n,m=map(int,input().split())
graph=[[] for i in range(3*n)]
for i in range(m):
    s,e=map(int,input().split())
    graph[s-1].append(e+n-1)
    graph[s+n-1].append(e+2*n-1)
    graph[s+2*n-1].append(e-1)
s,t=map(int,input().split())
s-=1;t-=1
queue=deque([s])
length=0
dist=[-1]*(3*n)
dist[s]=0
while queue:
    v=queue.popleft()
    for i in graph[v]:
        if dist[i]!=-1:continue
        dist[i]=dist[v]+1
        queue.append(i)
print(dist[t]//3)

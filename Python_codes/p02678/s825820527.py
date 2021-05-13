from collections import deque
n,m=map(int,input().split())
G=[[] for i in range(n+1)]# 隣接リスト

for i in range(m):# 隣接リストを格納
    a,b=map(int,input().split())
    templ=G[a]
    templ.append(b)
    G[a]=templ
    templ=G[b]
    templ.append(a)
    G[b]=templ


dist=[-1 for i in range(n+1)]
prev=[-1 for i in range(n+1)]
q=deque([1])
dist[1]=0

while len(q)!=0:
    v=q.popleft()
    for nv in G[v]:
        if dist[nv]!=-1:
            continue
        dist[nv]=dist[v]+1
        prev[nv]=v
        q.append(nv)
print('Yes')
for i in range(2,n+1):
    print(prev[i])


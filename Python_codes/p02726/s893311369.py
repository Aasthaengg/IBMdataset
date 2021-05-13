n,x,y=map(int,input().split())
edge=[None]*n
edge[0]=[1]
edge[n-1]=[n-2]
for i in range(1,n-1):
    edge[i]=[i-1,i+1]
edge[x-1].append(y-1)
edge[y-1].append(x-1)
ans=[0]*n

from collections import deque
def bfs(start):
    q=deque([start])
    d=[None]*n
    d[start]=0
    while q:
        v=q.popleft()
        for nv in edge[v]:
            if d[nv]==None:
                d[nv]=d[v]+1
                q.append(nv)
    for i in d:
        ans[i]+=1

for i in range(n):
    bfs(i)
for i in ans[1:]:
    print(i//2)
n,m=map(int,input().split())
lrd=[]
es=[[] for i in range(n)]
for i in range(m):
    l,r,d=map(int,input().split())
    lrd.append((l-1,r-1,d))
    es[l-1].append((d,r-1))
    es[r-1].append((-d,l-1))

from collections import deque
que=deque([])
dist=[float('inf')]*n

for i in range(n):
    if dist[i]==float('inf'):
        dist[i]=int(0)
        que.append(i)
        while que:
            p=que.popleft()
            for d, j in es[p]:
                if dist[j]==float('inf'):
                    dist[j]=int(dist[p]+d)
                    que.append(j)

for l,r,d in lrd:
    if dist[l]-dist[r]!=-d:
        print('No')
        exit()
print('Yes')

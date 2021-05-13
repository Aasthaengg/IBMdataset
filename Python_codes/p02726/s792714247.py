from collections import deque
n,x,y=map(int,input().split())
edge=[[] for _ in range(n)]
for i in range(n-1):
    edge[i+1].append(i)
    edge[i].append(i+1)
edge[x-1].append(y-1)
edge[y-1].append(x-1)
ans=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist=[-1]*n
    dist[i]=0
    que=deque([i])
    while que:
        now=que.popleft()
        for j in edge[now]:
            if dist[j]==-1:
                dist[j]=dist[now]+1
                que.append(j)
    for j in range(n):
        ans[i][j]=dist[j]
aa=[0]*n
for i in ans:
    for j in i:
        aa[j]+=1
for i in aa[1:]:
    print(i//2)
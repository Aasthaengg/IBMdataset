import queue
n,x,y=map(int,input().split())
edge=[[i-1,i+1] for i in range(n)]
edge[0],edge[-1]=[1],[n-2]
edge[x-1].append(y-1)
edge[y-1].append(x-1)
inf=10**6
ans=[0]*n
for i in range(n):
    q=queue.deque([i])
    dist=[inf]*n
    dist[i]=1
    while q:
        a=q.pop()
        for e in edge[a]:
            if dist[e]==inf:
                q.appendleft(e)
                dist[e]=dist[a]+1
    for v in dist:
        ans[v-1]+=1
for i in range(n-1):
    print(ans[i+1]//2)
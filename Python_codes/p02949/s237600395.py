n,m,p=map(int,input().split())
data=[list(map(int,input().split())) for i in range(m)]
inf=float("inf")
dist=[-inf]*(n+1)
dist[1]=0
for i in range(n-1):
    for a,b,c in data:
        if dist[a]!=-inf:
            dist[b]=max(dist[b],dist[a]+c-p)
lst=[]
for a,b,c in data:
    if dist[b]<dist[a]+c-p:
        lst.append(b)

tag=[[] for i in range(n+1)]
for a,b,c in data:
    tag[a].append(b)
flag=[0]*(n+1)
for u in lst:
    if flag[u]==0:
        flag[u]=1
        que=[u]
        while que:
            h=que.pop()
            for v in tag[h]:
                if flag[v]==0:
                    que.append(v)
                    flag[v]=1
if flag[n]==1:
    print(-1)
else:
    print(max(0,dist[n]))
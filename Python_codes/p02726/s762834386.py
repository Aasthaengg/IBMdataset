from collections import Counter,deque
def bfs(G,s,N):
    dist=[-1]*(N+1)
    d=deque()
    dist[s]=0
    d.append(s)
    while(len(d)!=0):
        v=d[0]
        d.popleft()
        for nv in G[v]:
            if(dist[nv]!=-1):
                continue
            #発見した地点への操作
            dist[nv]=dist[v]+1
            d.append(nv)
            #ここまで
    return dist

N,X,Y=map(int,input().split())
G=[[] for i in range(N+1)]
for i in range(1,N):
    G[i].append(i+1)
    G[i+1].append(i)
G[X].append(Y);G[Y].append(X)
Count=[0]*(N+1)
for i in range(1,N+1):
    li=bfs(G,i,N)
    c=Counter(li)
    for i in range(1,N+1):
        Count[i]+=c[i]
for i in range(1,N):
    print(Count[i]//2)

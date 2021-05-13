from collections import deque
def bfs(G,s,N):
    dist=[[-1]*N for i in range(3)]
    d=deque()
    dist[0][s]=0
    d.append((0,s))
    while(len(d)!=0):
        p,v=d.popleft()
        for np,nv in G[p][v]:
            if(dist[np][nv]!=-1):
                continue
            dist[np][nv]=dist[p][v]+1
            d.append((np,nv))
    return dist

N,M=map(int,input().split())
G=[[[] for i in range(N)] for i in range(3)]
for i in range(M):
    u,v=map(lambda x:int(x)-1,input().split())
    G[0][u].append((1,v))
    G[1][u].append((2,v))
    G[2][u].append((0,v))
S,T=map(lambda x:int(x)-1,input().split())
dist=bfs(G,S,N)
ans=dist[0][T]
print(ans//3 if ans!=-1 else ans)
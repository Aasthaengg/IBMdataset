INF=10**50

def Bellman_Ford(s,N,Edge):
    dist=[INF]*N
    dist[s]=0
    for i in range(N-1):
        for f,t,c in Edge:
            if dist[f]!=INF and dist[t]>dist[f]+c:
                dist[t]=min(dist[t],dist[f]+c)
    F=[False]*N
    for j in range(N):
        for f,t,c in Edge:
            if(dist[t]>dist[f]+c):
                dist[t]=dist[f]+c
                F[t]=True
    if F[N-1]:
        return 'inf'
    else:
        return -dist[N-1]
    
N,M=map(int,input().split())
Edge=[]
for i in range(M):
    a,b,c=map(int,input().split())
    a,b,c=a-1,b-1,-c
    Edge.append([a,b,c])
print(Bellman_Ford(0,N,Edge))
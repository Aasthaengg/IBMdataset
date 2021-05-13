INF=10**50

def Bellman_Ford(s,N,Edge):
    dist=[INF]*N
    dist[s]=0
    cnt=0
    while True:
        update=False
        for f,t,c in Edge:
            if dist[t]>dist[f]+c:
                if dist[f]!=INF:
                    dist[t]=min(dist[t],dist[f]+c)
                    update=True
                    if cnt==N-1 and t==N-1:
                        print('inf')
                        exit()
        if not update or cnt==N-1:
            break
        cnt+=1
    return -dist[N-1]
N,M=map(int,input().split())
Edge=[]
for i in range(M):
    a,b,c=map(int,input().split())
    a,b,c=a-1,b-1,-c
    Edge.append([a,b,c])
print(Bellman_Ford(0,N,Edge))
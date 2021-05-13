import itertools

N,M,R=map(int,input().split())
r=list(map(int,input().split()))
n=len(r)

graph=[[float("inf")]*N for _ in range(N)]
for i in range(M):
    A,B,C=map(int,input().split())
    A-=1
    B-=1
    graph[A][B]=C
    graph[B][A]=C

def dijkstra(start,cost):
    d=[float("inf")]*N
    used=[False]*N
    d[start]=0

    while True:
        v=-1
        for i in range(N):
            if (not used[i]) and (v==-1):
                v=i
            elif (not used[i]) and d[i]<d[v]:
                v=i
        if v==-1:
            break
        used[v]=True

        for j in range(N):
            d[j]=min(d[j],d[v]+cost[v][j])
    
    return d

d=[]
for i in range(N):
    d.append(dijkstra(i,graph))

ans=float("inf")
for city in itertools.permutations(r):
    tmp=0
    for i in range(n-1):
        tmp+=d[city[i]-1][city[i+1]-1]
    ans=min(ans,tmp)
print(ans)
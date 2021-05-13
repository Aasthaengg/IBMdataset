import sys
input=sys.stdin.readline

def Warshall_Floyd(N,DIST):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                DIST[i][j]=min(DIST[i][j],DIST[i][k]+DIST[k][j])
    return DIST

N,M,L=map(int,input().split())

ABC=[list(map(int,input().split())) for i in range(M)]

Q=int(input())

st=[list(map(int,input().split())) for i in range(Q)]

inf=L+1
dist=[[inf]*N for i in range(N)]
for i in range(N):
    dist[i][i]=0
for A,B,C in ABC:
    dist[A-1][B-1]=min(dist[A-1][B-1],C)
    dist[B-1][A-1]=min(dist[B-1][A-1],C)

dist=Warshall_Floyd(N,dist)
dist_2=[[N+1]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if dist[i][j]<=L:
            dist_2[i][j]=1
            
for i in range(N):
    dist_2[i][i]=0

dist_2=Warshall_Floyd(N,dist_2)

for s,t in st:
    if dist_2[s-1][t-1]==N+1:
        print(-1)
    else:
        print(dist_2[s-1][t-1]-1)
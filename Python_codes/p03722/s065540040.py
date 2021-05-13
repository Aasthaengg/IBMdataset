import sys
N,M=map(int,input().split())
edge=[]
for i in range(M):
    a,b,c=map(int,input().split())
    edge.append([a-1,b-1,-c])
inf=10**30
dist=[inf]*N
dist[0]=0
for i in range(N+1):
    for x,y,z in edge:
        if dist[y]<= dist[x]+z:
            continue
        dist[y]=dist[x]+z
        if i==N and y==N-1:
            print('inf')
            sys.exit()
print(-dist[N-1])

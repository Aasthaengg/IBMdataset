
from copy import copy
N=int(input())
G=[[] for _ in range(N)]
di=[-1]*N
for i in range(N-1):
    u,v,w=map(int,input().split())
    G[u-1].append([v-1,w])
    G[v-1].append([u-1,w])

di[0]=0
for g,w in G[0]:
    di[g]=w

for i in range(1,N):
    if di[i]!=-1:continue
    seen=[0]*N
    stack=copy(G[0])
    seen[0]=1
    dis=0
    while stack:
        y,d=stack.pop()
        if seen[y]==1:continue
        seen[y]=1
        if y==i:
            di[i]=dis+d
            break
        else:
            for z,dist in G[y]:
                if seen[z]==0:
                    di[z]=dis+d+dist
                    stack.append([z,dis+d+dist])

for i in range(N):
    if di[i]%2==0:
        print(0)
    else:
        print(1)
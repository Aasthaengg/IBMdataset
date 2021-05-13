from _collections import deque
import sys
sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
ab=[[0,0]  for i in range(m)]
for i in range(m):
    ab[i][0],ab[i][1]=map(int,input().split())
ans=0
for i in range(m):
    edg=[[] for j in range(n+1)]
    for j in range(m):
        if j!=i:
            a,b=ab[j][0],ab[j][1]
            edg[a].append(b)
            edg[b].append(a)
    che=[0]*(n+1)
    che[0]=1
    def search(x):
        che[x]=1
        for j in edg[x]:
            if che[j]==0:
                search(j)
    search(1)
    if not all(che[j]==1 for j in range(n+1)):
        ans+=1
print(ans)


import sys
from collections import *
sys.setrecursionlimit(10**5)
def dfs(x):
    visited[x]=True
    for i in range(len(adj[x])):
        t=adj[x][i]
        distance[t]=max(distance[t],distance[x]+1)
        indegree[t]-=1
        if(indegree[t]==0):
            dfs(t)

MAX = 10**5+5
indegree=[0]*(MAX)
distance=[0]*(MAX)
visited = [False]*(MAX)
adj = defaultdict(list)
N,M=list(map(int,input().split()))
for i in range(M):
    a,b=list(map(int,input().split()))
    adj[a].append(b)
    indegree[b]+=1
ans=0
for i in range(1,N+1):
    if(visited[i]==False and indegree[i]==0):
        dfs(i)
for i in range(1,N+1):
    ans=max(ans,distance[i])

print(ans)

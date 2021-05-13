import sys
sys.setrecursionlimit(10**9)

N=int(input())
graph=[[] for _ in range(N)]
for i in range(N-1):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a].append([b,c])
    graph[b].append([a,c])

def dfs(start):
    for x,cost in graph[start]:
        if d[x]==-1:
            d[x]=d[start]+cost
            dfs(x)

Q,K=map(int,input().split())
K-=1
d=[-1]*N
d[K]=0
dfs(K)
for i in range(Q):
    x,y=map(int,input().split())
    x-=1
    y-=1
    print(d[x]+d[y])
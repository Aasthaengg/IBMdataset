import sys
sys.setrecursionlimit(2000000)

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,w = map(int,input().split())
    edges[u].append((v,w))
    edges[v].append((u,w))
color = [-1]*(N+1)
def dfs(n,p,c):
    color[n]=c
    for nx,w in edges[n]:
        if nx != p:
            if w % 2 == 0:
                nxC = c
            else:
                nxC = (c+1)%2
            dfs(nx,n,nxC)

dfs(1,0,0)
for i in range(1,N+1):
    print(color[i])
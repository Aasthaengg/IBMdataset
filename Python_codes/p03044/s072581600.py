import sys
sys.setrecursionlimit(10**7)
n=int(input())
edge=[[] for _ in range(n)]
dist=[-1]*n
for i in range(n-1):
    x,y,z=map(int,input().split())
    edge[x-1].append([y-1,z])
    edge[y-1].append([x-1,z])
def dfs(node,d):
    dist[node]=d
    for i in edge[node]:
        if dist[i[0]]==-1:
            dfs(i[0],d+i[1])
dfs(0,0)
print(*[i%2 for i in dist],sep='\n')
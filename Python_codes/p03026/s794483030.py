import sys
sys.setrecursionlimit(10**7)
def dfs(v,p):
    ans[v]=c.pop()
    for nv in G[v]:
        if nv==p:
            continue
        dfs(nv,v)

N=int(input())
G=[[] for i in range(N)]

for i in range(N-1):
    a,b=map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)
c=sorted(map(int,input().split()))
print(sum(c[:-1]))
ans=[-1]*N
dfs(0,-1)
print(*ans)
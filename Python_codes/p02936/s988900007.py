import sys
sys.setrecursionlimit(10**7) 

N,Q = map(int,input().split())
path = [[] for i in range(N)]
ans = [0] * N
def dfs(v,p=-1):
    for to in path[v]:
        if to == p :
            continue
        ans[to] += ans[v]
        dfs(to,v)

for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)
for i in range(Q):
    P,X = map(int,input().split())
    ans[P-1] += X
dfs(0)
print(*ans)
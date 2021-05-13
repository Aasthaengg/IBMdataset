import sys
 
sys.setrecursionlimit(100000)
 
N, M = map(int, input().split(" "))
G = [[] for _ in range(N)]
 
for _ in range(M):
    x, y = map(int, input().split(" "))
    G[x-1].append(y-1)
dp = [-1] * N
def pathlen(G, dp, v):
    if dp[v] != -1:
        return dp[v]
 
    plen = 0
    for i in G[v]:
        plen = max(plen, pathlen(G, dp, i)+1)
    dp[v] = plen
    return plen
ans = 0
for i in range(N):
    ans = max(ans, pathlen(G, dp, i))
print(ans)
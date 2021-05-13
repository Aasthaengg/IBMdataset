import sys
sys.setrecursionlimit(10**8)
(n,m),*xy = [list(map(int,r.split())) for r in open(0)]
g = [[] for _ in range(n)]
dp = [0 for _ in range(n)]

for i in xy:
    x,y = i[0],i[1]
    x -= 1
    y -= 1
    g[y].append(x)

def rec(node):
    if dp[node] > 0:
        return dp[node]
    
    if not g[node]:
        dp[node] = 0
        return 0

    for child in g[node]:
        dp[node] = max(dp[node], rec(child) + 1)

    return dp[node]

ans = 0
for i in range(n):
    ans = max(ans, rec(i))
print(ans)

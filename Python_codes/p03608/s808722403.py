from itertools import permutations
N,M,R = map(int,input().split())
r = list(map(lambda x:int(x)-1,input().split()))
edges = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].append((b,c))
    edges[b].append((a,c))
V = N
INF = float("inf")
dp = [[INF]*V for _ in range(V)]
for i in range(V):
    for j, w in edges[i]:
        dp[i][j] = w
for k in range(V):
    for i in range(V):
        for j in range(V):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

ans = INF
for p in permutations(r):
    t = 0
    for i in range(1, R):
        t += dp[p[i]][p[i-1]]
    ans = min(ans, t)
print(ans)
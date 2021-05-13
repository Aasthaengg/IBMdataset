n, m, r = map(int, input().split())
R = tuple(map(lambda x: int(x)-1, input().split()))
INF = 10**9
dp = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = c
    dp[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

from itertools import permutations
ans = INF
for p in permutations(R):
    dist = 0
    for i in range(r-1):
        dist += dp[p[i]][p[i+1]]
    ans = min(ans, dist)
print(ans)
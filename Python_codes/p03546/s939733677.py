def floyd_warshall(dp, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

H, W = [int(x) for x in input().split()]
c = [[int(x) for x in input().split()] for _ in range(10)]
A = [[int(x) for x in input().split()] for _ in range(H)]

c = floyd_warshall(c, 10)

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1: continue
        ans += c[A[i][j]][1]

print(ans)
INF = 10**9

H, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [INF for i in range(H+1)]

dp[0] = 0

for i in range(N):
    a = AB[i][0]
    b = AB[i][1]
    for j in range(H+1):
        next_j = min(j+a, H)
        dp[next_j] = min(dp[next_j], dp[j]+b)

print(dp[H])
N, K = map(int, input().split())
H = list(map(int, input().split()))

H = [0] + H
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + abs(H[i]-H[i-1])
    for k in range(2, K+1):
        if i-k >= 1:
            dp[i] = min(dp[i], dp[i-k]+abs(H[i]-H[i-k]))

res = dp[N]
print(res)
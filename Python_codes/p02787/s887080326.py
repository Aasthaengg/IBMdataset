H, N = map(int, input().split())
AB = [0] * N
for i in range(N):
    AB[i] = list(map(int, input().split()))

m = 10**4 + 100

dp = [float("INF")] * m

dp[0] = 0

for i in range(H):
    for x in AB:
        if i + x[0] <= H:
            dp[i + x[0]] = min(dp[i + x[0]], dp[i] + x[1])
        else:
            dp[H] = min(dp[H], dp[i] + x[1])

print(dp[H])
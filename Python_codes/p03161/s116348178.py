N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [float('inf')] * (N)
dp[0] = 0

for i in range(1, N):
    min_from = max(0, i - K)

    temp = float('inf')
    for j in range(min_from, i):
        temp = min(temp, dp[j] + abs(H[i] - H[j]))
    dp[i] =temp

print(dp[N-1])


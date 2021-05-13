N,K = map(int, input().split())
H = list(map(int, input().split()))

dp = [0] * N

for n in range(1, N):
    dp[n] = min(dp[k] + abs(H[n] - H[k]) for k in range(max(0, n-K), n))

print(dp[-1])
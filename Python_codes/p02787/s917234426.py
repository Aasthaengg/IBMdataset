H, N = map(int, input().split())
AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append([A, B])
dp = [10**9] * (H + 1)
dp[0] = 0
for i in range(H):
    for a, b in AB:
        if i + a <= H:
            dp[i + a] = min(dp[i + a], dp[i] + b)
        else:
            dp[H] = min(dp[H], dp[i] + b)
print(dp[H])

n, k = map(int, input().split())
h = list(map(int, input().split()))

def chmin(a, b):
    if a > b: return b
    else: return a

dp = [float('inf')] * (n + k)
dp[0] = 0
for i in range(n):
    for j in range(1, k + 1):
        if i + j < n:
            dp[i + j] = chmin(dp[i + j], dp[i] + abs(h[i] - h[i + j]))
print(dp[n - 1])
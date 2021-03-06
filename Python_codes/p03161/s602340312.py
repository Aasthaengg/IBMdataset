n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0]= 0

for i in range(n):
    for j in range(k+1):
        if i + j < n:
            dp[i+j] = min(dp[i+j], dp[i] + abs(h[i+j] - h[i]))

print(dp[-1])
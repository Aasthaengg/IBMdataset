n = int(input())
hs = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(n):
    if i == 0:
        continue
    prev_abs = abs(hs[i] - hs[i-1])
    if i == 1:
        dp[i] = prev_abs
    else:
        dp[i] = min(dp[i-2] + abs(hs[i] - hs[i-2]), dp[i-1] + prev_abs)

print(dp[n-1])
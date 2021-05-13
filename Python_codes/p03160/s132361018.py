n = int(input())
hs = [int(x) for x in input().split()]
dp = [0 for _ in range(n+1)]
dp[2] = abs(hs[1] - hs[0])
for i in range(3, n + 1):
    one = dp[i-2] + abs(hs[i-1] - hs[i-3])
    two = dp[i-1] + abs(hs[i-1] - hs[i-2])
    dp[i] = min(one, two)
print(dp[n])

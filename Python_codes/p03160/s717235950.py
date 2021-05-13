n = int(input())
dat = list(map(int, input().split()))
inf = 10**10
dp = [inf] * (n + 10)
dp[0] = 0
for i in range(n):
    if i+1 > n-1:
        continue
    dp[i+1] = min(dp[i+1], dp[i] + abs(dat[i] - dat[i+1]))
    if i+2 > n-1:
        continue
    dp[i+2] = min(dp[i+2], dp[i] + abs(dat[i] - dat[i+2]))
print(dp[n-1])

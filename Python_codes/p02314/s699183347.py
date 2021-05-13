n, m = map(int, input().split())

c = list(map(int, input().split()))
c.sort()

inf = float("inf")
dp = [inf for _ in range(n+1)] #最小化問題の時はinfのほうが良いのかな
dp[0] = 0

for i in range(1, n+1):
    for j in range(m):
        if i >= c[j]:
            dp[i] = min(dp[i-c[j]]+1, dp[i])
        else:
            dp[i] = dp[i]


print(dp[n])

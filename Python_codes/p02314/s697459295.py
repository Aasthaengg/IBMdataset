inf = 10 ** 20
n,m = map(int,input().split())
c = [int(i) for i in input().split()]
dp = [inf for _ in range(n + 1)]
dp[0] = 0
for coin in c:
    for j in range(n + 1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j - coin] + 1)
print(dp[n])


h, n = map(int, input().split())
AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))

INF = 10**18
dp = [INF]*(h+1)
dp[h] = 0
for i in reversed(range(h+1)):
    for j in range(n):
        a,b = AB[j]
        if i-a >= 0:
            dp[i-a] = min(dp[i-a], dp[i]+b)
        else:
            dp[0] = min(dp[0], dp[i]+b)
print(dp[0])

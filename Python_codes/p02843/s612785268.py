x = int(input())
dp = [0] * (x+1)
dp[0] = 1
for i in range(1,x+1):
    for t in range(100,106):
        if i - t >= 0:
            dp[i] = max(dp[i], dp[i-t])
print(dp[x])
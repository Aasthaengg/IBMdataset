x = int(input())
dp = [0]*(x+105)
dp[0] = 1
for i in range(x):
    for j in range(6):
        dp[i+100+j] = dp[i+100+j] | dp[i]
print(dp[x])
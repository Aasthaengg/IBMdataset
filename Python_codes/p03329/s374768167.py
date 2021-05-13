dp = [999999] * 100100
n = int(input())
dp[0] = 0
for i in range(0, 100010):
    dp[i+1] = min(dp[i+1], dp[i] + 1)
    for j in range(1,100):
        c = i + 6**j
        if (c) > 100000:
            break
        dp[c] = min(dp[c], dp[i] + 1)

    for j in range(1,100):
        c = i + 9**j
        if (c) > 100000:
            break
        dp[c] = min(dp[c], dp[i] + 1)

#print(dp[:100])
print(dp[n])
n = int(input())
dp = [float("Inf")]*(n+1)
for i in range(min(6, n+1)):
    dp[i] = i
for i in range(n):
    for j in range(1,n//6+1):
        if i + 6**j > n:
            break
        dp[i+6**j] = min(dp[i+6**j], dp[i] + 1)
    for j in range(1,n//9+1):
        if i + 9**j > n:
            break
        dp[i+9**j] = min(dp[i+9**j], dp[i] + 1)
print(dp[-1])
n = int(input())
dp = [float("Inf")]*(n+1)
dp[0] = 0
for i in range(n):
    if dp[i] == float("Inf"):
        pass
    else:
        for j in range(1,n//6+1):
            if i + 6**j > n:
                break
            dp[i+6**j] = min(dp[i+6**j], dp[i] + 1)
        for j in range(1,n//9+1):
            if i + 9**j > n:
                break
            dp[i+9**j] = min(dp[i+9**j], dp[i] + 1)
ans = n
for i in range(max(0, n-5), n+1):
    ans = min(ans, dp[i]+n-i)
print(ans)
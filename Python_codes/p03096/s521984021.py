n = int(input())
c = [0] * (n + 1)

for i in range(1, n + 1):
    c[i] = int(input())
    
lc = [0] * (2 * 10**5 + 1)
dp = [0] * (n + 1)
dp[1] = 1
lc[c[1]] = 1

for i in range(2, n + 1):
    if lc[c[i]] == i - 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[lc[c[i]]]
    lc[c[i]] = i
    
print(dp[n] % (10**9 + 7))
n = int(input())
a = [int(input()) for _ in range(n)]
MOD = 10**9+7

na = [a[0]]
for i in range(n-1):
    if a[i] != a[i+1]:
        na.append(a[i+1])
        
m = len(na)
cur = [-1]*(max(na)+1)

dp = [0]*(m+1)
dp[0] = 1
for i in range(m):
    if cur[na[i]] != -1:
        dp[i+1] = (dp[i] + dp[cur[na[i]]]) % MOD
        cur[na[i]] = i+1
    else:
        cur[na[i]] = i+1
        dp[i+1] = dp[i]
        
print(dp[m])
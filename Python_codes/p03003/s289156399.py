mod = 10**9+7
n, m = list(map(int,input().split()))
s = list(map(int,input().split()))
t = list(map(int,input().split()))
dp = [0]*(m+1)
for i in range(n)[::-1]:
    old = 0
    for j in range(m)[::-1]:
        tmp = dp[j] + dp[j+1] - old
        tmp %= mod
        if s[i]== t[j]:
            tmp += 1 + old
            tmp %= mod
        dp[j], old = tmp, dp[j]
print((dp[0]+1)%mod)
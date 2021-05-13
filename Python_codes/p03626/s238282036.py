n = int(input())
s1 = input()
s2 = input()
mod = 1000000007
dp = [0]*n
dp[0] = 3 if s1[0] == s2[0] else 6
for i in range(1,n):
    if s1[i] == s1[i-1]: dp[i] = dp[i-1]
    elif s1[i-1] == s2[i-1]: dp[i] = dp[i-1]*2%mod
    elif s1[i] == s2[i]: dp[i] = dp[i-1]
    else: dp[i] = dp[i-1]*3%mod
print(dp[n-1])
n = int(input())
s = [list(input()), list(input())]

MOD = 1000000007

dp = [0]*n
if s[0][0] == s[1][0]: # tate
    dp[0] = 3
else: # yoko
    dp[0] = 6

for i in range(1,n):
    if s[0][i] == s[0][i-1]:
        dp[i] = dp[i-1]
    elif s[0][i-1] == s[1][i-1] and s[0][i] == s[1][i]: # tate & tate
        dp[i] = dp[i-1] * 2 % MOD
    elif s[0][i-1] == s[1][i-1] and s[0][i] != s[1][i]: # tate & yoko
        dp[i] = dp[i-1] * 2 % MOD
    elif s[0][i-1] != s[1][i-1] and s[0][i] == s[1][i]: # yoko & tate
        dp[i] = dp[i-1] 
    else: # yoko & yoko
        dp[i] = dp[i-1] * 3 % MOD
print(dp[n-1])
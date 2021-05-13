#071_D
n = int(input())
s = [input() for _ in range(2)]
mod = 10 ** 9 + 7

dp = [0 for _ in range(n)]
tate = [s[0][i] == s[1][i] for i in range(n)]

if tate[0]:
    dp[0] = 3
    x = 1
else:
    dp[0] = dp[1] = 6
    x = 2

while x < n:
    if tate[x-1] and tate[x]:
        dp[x] = (dp[x-1] * 2) % mod
    elif tate[x-1]:
        dp[x] = (dp[x-1] * 2) % mod
        dp[x+1] = dp[x]
        x += 1
    elif tate[x-1] == False and tate[x]:
        dp[x] = dp[x-1]
    else:
        dp[x] = (dp[x-1] * 3) % mod
        dp[x+1] = dp[x]
        x += 1
    x += 1
    
print(dp[n-1])
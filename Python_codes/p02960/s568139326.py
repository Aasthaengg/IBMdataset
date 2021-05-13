s = input()
n = len(s)
MOD = 10 ** 9 + 7

# 先頭i文字としてあり得る数のうち、13で割ったあまりがjである個数
dp = [[0] * 13 for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    if s[i] == '?':
        c = -1
    else:
        c = int(s[i])
    for d in range(10):
        if c != -1 and c != d:
            continue
        for j in range(13):
            dp[i+1][(10*j+d)%13] += dp[i][j]
    
    for j in range(13):
        dp[i+1][j] %= MOD
    
print(dp[n][5])

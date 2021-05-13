MOD = 10**9+7
s = input()
n = len(s)
dp = [[0]*13 for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    digit = n-1-i
    x = s[digit]
    X = []
    if x != '?':
        X.append(int(x)*pow(10, i, 13) % 13)
    else:
        for num in range(10):
            X.append(num*pow(10, i, 13) % 13)
    for j in range(13):
        for x in X:
            dp[i+1][(j+x) % 13] += dp[i][j]
            dp[i+1][(j+x) % 13] %= MOD

print(dp[-1][5])

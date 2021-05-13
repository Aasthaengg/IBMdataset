a = list(range(13))
b = []
for i in a:
    num = int(str(i) + '0') % 13
    l = []
    for j in range(13):
        l.append((num+j)%13)
    b.append(l)

s = input()
MOD = 10**9+7
dp = [[0 for _ in range(13)] for _ in range(len(s))]
if s[0] == '?':
    for i in range(10):
        dp[0][i] += 1
else:
    dp[0][int(s[0])] += 1

for i in range(1, len(s)):
    if s[i] == '?':
        for j in range(13):
            for k in range(10):
                dp[i][b[j][k]] += dp[i-1][j]
                dp[i][b[j][k]] %= MOD
    else:
        for j in range(13):
            n = b[j][int(s[i])]
            dp[i][n] += dp[i-1][j]
            dp[i][n] %= MOD
print(dp[-1][5]%MOD)

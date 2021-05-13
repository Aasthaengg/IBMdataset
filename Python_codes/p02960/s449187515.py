s = list(input())

MOD = pow(10, 9) + 7

n = len(s)

dp = [[0] * 13 for _ in range(n)]

#r = list(range(10))

#init
if s[-1] == "?":
    for j in range(10):
        dp[0][j] = 1
else:
    q = int(s[-1])
    dp[0][q] = 1

r = 1

for i in range(1, n):
    r = r * 10 % 13
    # for l in range(10):
    #     r[l] = r[l] * 10 % 13

    #print(r)

    if s[n-i-1] == "?":
        for j in range(10):
            q = j * r % 13
            for k in range(13):
                dp[i][k] += dp[i-1][k-q] % MOD
    
    else:
        q = int(s[n-i-1]) * r % 13
        #print(q)
        for k in range(13):
            dp[i][k] += dp[i-1][k-q] % MOD
    #print(dp[i])

print(dp[n-1][5] % MOD)
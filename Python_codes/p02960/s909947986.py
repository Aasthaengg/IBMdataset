import sys,queue,math,copy,itertools,bisect,collections
MOD = 10**9 + 7
S = sys.stdin.readline().rstrip()
dp = [[0] * 13 for _ in range(len(S)+1)]
dp[0][0] = 1

for i in range(1,len(S)+1):
    x = S[i-1]
    if x == '?':
        for j in range(10):
            for k in range(13):
                dp[i][(k * 10 + j) % 13] += dp[i - 1][k]
    else:
        for k in range(13):
            dp[i][(k * 10 + int(x)) % 13] += dp[i - 1][k]
    for j in range(13):
        dp[i][j] %= MOD

print (dp[-1][5])

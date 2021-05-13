# https://kato-robotics.hatenablog.com/entry/2019/07/28/204812

S = input()

MOD = 10 ** 9 + 7

dp = [[0]*13 for _ in range(len(S)+1)]
dp[0][0] = 1

for i in range(len(S)):
    if S[i] == '?':
        for x in range(10):
            for j in range(13):
                dp[i+1][(j * 10 + x) % 13] += dp[i][j]
    else:
        x = int(S[i])
        for j in range(13):
            dp[i+1][(j * 10 + x) % 13] += dp[i][j]
    
    for j in range(13):
        dp[i+1][j] %= MOD

print(dp[len(S)][5])
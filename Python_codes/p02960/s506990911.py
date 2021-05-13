S = str(input())

# 桁数
N = len(S)
MOD = 10**9 + 7

# dp[i][j] := Sの上からi桁目までを考えた時、それを13で割った余りがjになる方法の数
dp = [[0 for _ in range(13)]for _ in range(N + 1)]

# １桁目について
if S[0] == "?":
    # ?に0, 1, ..., 9を入れることができる
    for i in range(10):
        dp[1][i] = 1
else:
    dp[1][int(S[0])] = 1

# 1, 2, ..., N-1桁から、
# 2, 3, ..., N桁についての遷移を考える
for i in range(1, N):
    for j in range(13):
        if S[i] == "?":
            for k in range(10):
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
                dp[i + 1][(j * 10 + k) % 13] %= MOD
        else:
            dp[i + 1][(j * 10 + int(S[i])) % 13] += dp[i][j]
            dp[i + 1][(j * 10 + int(S[i])) % 13] %= MOD

print(dp[N][5] % MOD)

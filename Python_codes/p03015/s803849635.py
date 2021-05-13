L = input()
MOD = 10 ** 9 + 7

# dp[i][flg] := 上からi番目の桁まで見た時に、L以下であることがflg（未確定/確定）であるような、条件を満たす組み合わせの通り数
dp = [[0] * 2 for i in range(len(L) + 1)]
dp[0][0] = 1
for i, l in enumerate(L, start=1):
    if l == '0':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = (3 * dp[i - 1][1]) % MOD
    else:
        dp[i][0] = (2 * dp[i - 1][0]) % MOD
        dp[i][1] = (3 * dp[i - 1][1] + dp[i - 1][0]) % MOD

print(sum(dp[-1]) % MOD)

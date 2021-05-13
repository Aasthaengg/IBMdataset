mod = 10 ** 9 + 7
s = input()
dp = [[0] * 4 for _ in range(len(s) + 1)]
dp[0][0] = 1
# dp[sの何文字目まで見たか][未取得0->A取得1->B取得2->C取得3]

for i, ss in enumerate(s):
    for j in range(4):
        dp[i + 1][j] += dp[i][j] * (1 if ss != '?' else 3)
        # i文字目を取らないケース

    if ss == 'A':
        dp[i + 1][1] += dp[i][0]
    elif ss == 'B':
        dp[i + 1][2] += dp[i][1]
    elif ss == 'C':
        dp[i + 1][3] += dp[i][2]
    elif ss == '?':
        dp[i + 1][1] += dp[i][0]  # Aに変えた
        dp[i + 1][2] += dp[i][1]  # Bに変えた
        dp[i + 1][3] += dp[i][2]  # Cに変えた
    # i文字目を取るケース

    for j in range(4):
        dp[i + 1][j] %= mod

print(dp[len(s)][3])

"""
i文字目の文字で処理を場合分け
それぞれ、取る場合と取らない場合の処理を書く
'?'のときで、文字を取らない場合、
ABCに変える3パターンそれぞれで取らない処理を行うので、3倍になる
"""

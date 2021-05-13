def e_common_subsequence(N, M, S, T, MOD=10**9 + 7):
    # dp[i][j]: S[i], T[j] まで考慮したとき、この2つをペアにしたときの場合の数
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # S, T のどちらかを見ていない場合、空整数列のみが等しい整数列となる
    for i in range(N + 1):
        dp[i][0] = 1
    for j in range(M + 1):
        dp[0][j] = 1

    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                # S[i], T[j] までで作れた等しい整数列に対して
                # 1つ新しい要素を付け加えられる。よって次式のように和を取る
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
            else:
                # S[i], T[j] は付け加えられないので、その分引く
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + MOD
            dp[i + 1][j + 1] %= MOD
    return dp[N][M]

N, M = [int(i) for i in input().split()]
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]
print(e_common_subsequence(N, M, S, T))
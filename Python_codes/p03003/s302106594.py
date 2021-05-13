# dp[i][j] SとTの最後の文字を採用するような文字列の個数。これにより各DPテーブルの値が排反になる。元の文字列の最後を必ず採用するので
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [[0] * (M + 2) for _ in range(N + 2)]
sdp = [[0] * (M + 2) for _ in range(N + 2)]
dp[0][0] = 1
sdp[1][1] = 1
for i in range(N + 1):
    for j in range(M + 1):
        if i - 1 >= 0 and j - 1 >= 0 and S[i - 1] == T[j - 1]:
            dp[i][j] = sdp[i][j]
        sdp[i + 1][j + 1] = sdp[i + 1][j] + sdp[i][j + 1] - sdp[i][j] + dp[i][j]
        sdp[i + 1][j + 1] %= MOD
        sdp[i + 1][j + 1] %= MOD
print(sdp[N + 1][M + 1])

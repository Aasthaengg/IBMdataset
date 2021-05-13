# 解説AC
N,M = map(int, input().split())
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]

MOD = 10 ** 9 + 7

# dp[i][j]: S[:i]とT[:j]の共通部分列のうち、
# S[i - 1] == T[j - 1]で、これを選ぶ場合の個数
dp = [[0] * (M + 1) for _ in range(N + 1)]

# DPの二次元累積和
sdp = [[0] * (M + 1) for _ in range(N + 1)]

# 初期条件
dp[0][0] = 1
for i in range(N + 1):
    sdp[i][0] = 1
for j in range(M + 1):
    sdp[0][j] = 1

for i, s in enumerate(S):
    for j, t in enumerate(T):
        if s == t:
            dp[i + 1][j + 1] = sdp[i][j]
        sdp[i + 1][j + 1] = sdp[i + 1][j] + sdp[i][j + 1] - sdp[i][j] + dp[i + 1][j + 1]
        sdp[i + 1][j + 1] %= MOD

print(sdp[N][M])
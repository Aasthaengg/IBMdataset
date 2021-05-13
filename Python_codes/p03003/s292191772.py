# https://atcoder.jp/contests/abc130/tasks/abc130_e
"""
タグ: LCS、二次元累積和
"""
import sys
input = sys.stdin.readline
MOD = 10**9 + 7

N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
cum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        if S[i]==T[j]:
            dp[i][j] += cum[i][j] + 1
            dp[i][j]%=MOD
        cum[i + 1][j + 1] = cum[i][j + 1] + cum[i + 1][j] - cum[i][j] + dp[i][j]
        cum[i + 1][j + 1]%=MOD
print(cum[N][M]+1)
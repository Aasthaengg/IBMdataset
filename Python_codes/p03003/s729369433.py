import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M = MI()
S = [0] + LI()
T = [0] + LI()
mod = 10**9+7

dp = [[0]*(M+1) for _ in range(N+1)]
# dp[i][j] = S[:i+1] と T[:j+1] に対する答え

for i in range(1,N+1):
    for j in range(1,M+1):
        if S[i] == T[j]:
            dp[i][j] = dp[i-1][j]+dp[i][j-1]+1
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
        dp[i][j] %= mod

print(dp[N][M]+1)  # 空列を追加

import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,S = MI()
A = [0] + LI()
mod = 998244353

dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(S+1):
        if j >= A[i]:
            dp[i][j] = 2*dp[i-1][j] + dp[i-1][j-A[i]]
            dp[i][j] %= mod
        else:
            dp[i][j] = 2*dp[i-1][j]
            dp[i][j] %= mod

print(dp[-1][-1])

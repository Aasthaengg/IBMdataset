N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

MOD = 10**9+7

dp = [[0 for i in range(M+1)] for j in range(N+1)] # dp[i][j] : S[i]とT[j]が末尾に来る部分集合の数
dp_sum = [[0 for i in range(M+1)] for j in range(N+1)] # dp[i][j]の総和

# 一旦空集合＋空集合は考えない
ret = 0
for i, s in enumerate(S):
    for j, t in enumerate(T):
        if s == t:
            dp[i+1][j+1] = dp_sum[i][j] + 1 # S[i]とT[j]を使ってないものの総和にS[i]とT[j]だけの組み合わせを足す
        dp_sum[i+1][j+1] = (dp[i+1][j+1] + dp_sum[i][j+1] + dp_sum[i+1][j] - dp_sum[i][j]) % MOD
        
print(dp_sum[N][M]+1)#最後に空集合＋空集合を加える


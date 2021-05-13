S = str(input())

Dp = [[0 for _ in range(13)] for _ in range(len(S)+1)]
Dp[0][0] = 1

mod = 1000000007

for i in range(len(S)):
    for j in range(13): # 遷移前のインデックス
        if S[i] != "?":
            Dp[i+1][(j*10+int(S[i]))%13] += Dp[i][j]
        else:
            for k in range(10):
                Dp[i+1][(j*10+k)%13] += Dp[i][j]
    for j in range(13):
        Dp[i+1][j] = Dp[i+1][j]%mod
        
print(Dp[-1][5])
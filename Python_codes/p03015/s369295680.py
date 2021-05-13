L = input()
L_bi = L
keta = len(L)
mod = 1000000007

dp = [[0 for _ in range(2)] for _ in range(1000002)]
dp[0][1]=1

for i in range(len(L_bi)):
    for j in range(2):
        if j == 1:
            scale = 2
        else:
            scale = 1
        dp[i+1][0] = (dp[i+1][0] + scale*dp[i][0])%mod
        if int(L_bi[i]) > j:
            dp[i+1][0] = (dp[i+1][0] + scale*dp[i][1])%mod
        elif int(L_bi[i]) == j:
            dp[i+1][1] = (dp[i+1][1] + scale*dp[i][1])%mod
print((dp[len(L_bi)][0]+dp[len(L_bi)][1])%mod)
H,W = map(int,input().split())
DP_1 = ["."*(W+1)]
for _ in range(H):
    A = "."+input()
    DP_1.append(A)
dp = [[0 for j in range(W+1)] for i in range(H+1)]
dp[0][1]=1
for i in range(1,H+1):
    for j in range(1,W+1):
        if DP_1[i][j]=="#":
            dp[i][j]=0
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[H][W]%(10**9+7))
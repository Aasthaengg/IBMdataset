MOD = 1000000007
H, W, K = map(int,input().split())
K -= 1

f_dic = {}
def f(x):
    if x in f_dic:
        return f_dic[x]
    elif x == 0:
        f_dic[0]=1
        return f_dic[0]
    elif x == 1:
        f_dic[1]=1
        return f_dic[1]
    else:
        f_dic[x] = f(x-1)+f(x-2)
        return f_dic[x]


if W == 1:
    print(1)

else:
    dp = [[0 for j in range(W)] for i in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        dp[i+1][0] += f(W-1)*dp[i][0]
        dp[i+1][1] += f(W-2)*dp[i][0]
        for j in range(1,W-1):
            dp[i+1][j-1] += f(j-1)*f(W-j-1)*dp[i][j]
            dp[i+1][j]   += f(j)  *f(W-j-1)*dp[i][j]
            dp[i+1][j+1] += f(j)  *f(W-j-2)*dp[i][j]
        dp[i+1][W-2] += f(W-2)*dp[i][W-1]
        dp[i+1][W-1] += f(W-1)*dp[i][W-1]
        for j in range(W):
            dp[i+1][j] %= MOD
    print(dp[H][K])

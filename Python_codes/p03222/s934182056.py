H, W, K = map(int, input().split())
dp = [[0 for i in range(W)] for j in range(H+1)]
mod = 10**9+7
dp[0][0] = 1

if W == 1:
    print(1)
else:
    for k in range(H):
        for i in range(2**(W-1)):
            b = format(i, "0{}b".format(W-1))
            flag = 1
            for j in range(len(b)-1):
                if b[j+1] == "1" and b[j] == "1":
                    flag = 0
                    break
            if flag == 0:
                continue

            for j in range(len(b)):
                if flag == 0:
                    flag = 1
                    continue
                if b[j] == "1":
                    dp[k+1][j+1] += dp[k][j]
                    dp[k+1][j] += dp[k][j+1]
                    dp[k+1][j+1] %= mod
                    dp[k+1][j] %= mod
                    flag = 0
                else:
                    dp[k+1][j] += dp[k][j]
                    dp[k+1][j] %= mod
            if b[-1] == "0":
                dp[k+1][-1] += dp[k][-1]
                dp[k+1][-1] %= mod
    print(dp[H][K-1])

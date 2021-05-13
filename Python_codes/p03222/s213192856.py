H, W, K = map(int, input().split())
MOD = 10 ** 9 + 7
if W == 1:
    print(1)
    exit()
ladder = W - 1
num_lad = [0] * ladder
limit = 0 #ハシゴの掛け方の総数
for i in range(2 ** ladder):
    flag = True
    for j in range(ladder-1):
        if (i >> j) & 1 and (i >> j+1) & 1:
            flag = False
    if not flag:
        continue
    limit += 1
    for j in range(ladder):
        # iのbitをj右にシフトしたらフラグが立っているかチェック
        if ((i >> j) & 1):
            num_lad[j] += 1

dp = [[0] * W for _ in range(H+1)]
dp[0][0] = 1

for i in range(1, H+1):
    for j in range(W):
        if j == 0:
            dp[i][j] = (dp[i-1][j] * (limit - num_lad[0]) + dp[i-1][j+1] * num_lad[0]) % MOD
        elif j == (W-1):
            dp[i][j] = (dp[i-1][j] * (limit - num_lad[ladder-1]) + dp[i-1][j-1] * num_lad[ladder-1]) % MOD
        else:
            dp[i][j] = (dp[i-1][j] * (limit - num_lad[j-1] - num_lad[j]) + \
                    dp[i-1][j+1] * num_lad[j] + dp[i-1][j-1] * num_lad[j-1]) % MOD

print(dp[H][K-1])

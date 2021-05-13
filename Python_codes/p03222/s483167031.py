import numpy as np
H, W, K = map(int, input().split())

if W == 1:
    print (1)
    exit()
MOD = 10 ** 9 + 7

#dp-tableの作成
lst = [[0] * (W) for i in range(H+2)]
dp = np.array(lst)
dp[0][0] = 1

def check(h): #h番目のX, Y, Zを検索
    count = 0
    for i in range(2**(W-1)):
        flag2 = True
        flag = False #一つ前が橋のとき、フラグをTrueにする
        for j in range(W-1):
            if flag2: #どこかで連続橋になったらそれ以降計算しない
                # print (j, end = ' ')
                if (i >> j) & 1: #1を橋とする
                    if flag: #連続で橋の時
                        count += 1
                        # print ('A', end = ' ')
                        flag = True
                        flag2 = False
                        break
                    else: #一つ前が橋では無い時-->ここに橋をかける
                        dp[H+1][j] += dp[h-1][j+1]%MOD
                        dp[H+1][j+1] += dp[h-1][j]%MOD
                        flag = True
                else:
                    if j == W-2: #最後の一本が橋でない時
                        dp[H+1][j+1] = dp[h-1][j+1]%MOD
                    if not flag: #連続で橋がかからない時、まっすぐ下ろす
                        dp[H+1][j] = dp[h-1][j]%MOD
                    else:
                        pass
                    flag = False
        if flag2: #最後まで条件を満たしていたら、H+1に記録していたものを通常の場所に移す
            dp[h][:] += dp[H+1][:]%MOD
            dp[h][:] = dp[h][:]%MOD
            # print (dp[H+1])
        dp[H+1][:] = 0
        # print ()
    # print (i)
    # print (count)
    return 0;

for i in range(H):
    check(i+1)

# print (dp)
print (dp[H][K-1]%MOD)

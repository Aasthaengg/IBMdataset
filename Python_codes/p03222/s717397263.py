MOD = 10**9 + 7

H, W, K = map(int, input().split())
if W == 1:
    print(1)
    exit()
dp = [[0 for x in range(W)] for h in range(H+1)]
dp[0][0] = 1

# ループを回す
for h in range(H):
    X, Y, Z = 0, 0, 0

    # 0: 線あり、1: 線なし
    for i in range(2 ** (W-1)):
        # 連続した1がある→隣接する列に線が引かれている
        if bin(i).count('11') >= 1:
            continue
        perm = [k for k in range(W)]
        for j in range(W-1):
            if ((i >> j) & 1):
                perm[j], perm[j+1] = perm[j+1], perm[j]

        for j in range(W):
            dp[h+1][perm[j]] += dp[h][j]
            dp[h+1][perm[j]] %= MOD


# 答えを得て出力
print(dp[H][K-1])
# print(dp)

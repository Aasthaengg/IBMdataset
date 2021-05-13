R, C, K = map(int, input().split())
item = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    item[r][c] = v


dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]

for i in range(R+1):
    for j in range(C+1):
        for k in range(4):
            here = dp[k][i][j]
            # 次の"行"に移動する場合（下に移動するので今まで獲得したアイテムの個数はリセットされる）
            if i + 1 <= R:
                # 移動先のアイテムを取らない場合
                dp[0][i+1][j] = max(dp[0][i+1][j], here)
                # 移動先のアイテムをとる場合
                dp[1][i+1][j] = max(dp[1][i+1][j], here+item[i+1][j])
            # 次の列に移動する場合（右に移動するのでその行で獲得したアイテムの個数は維持される）
            if j + 1 <= C:
                dp[k][i][j+1] = max(dp[k][i][j+1], here)
                # 現在のkが3未満のときのみ，移動先のアイテムをとることが可能
                if k < 3:
                    dp[k+1][i][j+1] = max(dp[k+1][i][j+1], here+item[i][j+1])

ans = 0
for k in range(4):
    ans = max(ans, dp[k][-1][-1])
print(ans)

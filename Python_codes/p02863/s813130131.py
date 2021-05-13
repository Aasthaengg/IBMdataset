N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
# 時間でソート
# 食べる料理が決まっている時、時間が最大のものを最後に頼むのが最適
AB.sort(key=lambda x: x[0])

# dp[i][j]=(i番目までの料理をj分以下で食べ切れるように選んだときの、美味しさの総和の最大値)
dp = [[0 for _ in range(T)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(T):
        # i番目の料理を食べることができる場合
        if j - AB[i - 1][0] >= 0:
            # 実際に料理を食べる場合、食べない場合
            dp[i][j] = max(dp[i - 1][j - AB[i - 1][0]] + AB[i - 1][1], dp[i - 1][j])
        # i番目の料理を食べることができない場合
        else:
            dp[i][j] = dp[i - 1][j]

ans = 0
# k番目の料理を最後に食べると考える(T-1分に注文する)
# k-1番目までの料理をT-1分の間に最適に食べる + k番目を食べる
for k in range(1, N + 1):
    tmp = dp[k - 1][T - 1] + AB[k - 1][1]
    ans = max(ans, tmp)

print(ans)

# コイン問題
# 個数制限なしナップサックで解く
N, M = map(int, input().split())  # N円, M種類の硬貨
C = list(map(int, input().split()))
dp = [[10**10]*(N+1) for _ in range(M+1)]  # m種類目までの硬貨を使ってn円払うときの最小枚数

dp[0][0] = 0
# M種類の中のi番目のコインを使う
for i in range(M):
    for j in range(N+1):
        # 使わない場合
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        # 使う場合
        if j + C[i] > N:  # 今i番目のコインを使った時にN円を超えるようならダメ
            continue
        # dp[i+1][j]+1は同じ段からの遷移を表している
        dp[i+1][j+C[i]] = min(dp[i][j]+1, dp[i+1][j]+1)
print(dp[M][N])


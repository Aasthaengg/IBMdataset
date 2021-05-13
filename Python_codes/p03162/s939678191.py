N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for i in range(N)]

# i日目にjを選択した時の最大値を計算する
for i in range(N):
    for j in range(3):
        if i == 0:
            dp[i][j] = array[i][j]
            continue
        for k in range(3):
            if j != k:
                sum = dp[i - 1][k] + array[i][j]
                dp[i][j] = sum if sum > dp[i][j] else dp[i][j]

print(max(dp[N - 1]))

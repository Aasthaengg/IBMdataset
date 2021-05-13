N, M = map(int, input().split())
A = list(map(int, input().split()))

# num[i] = iを作るために必要なマッチの本数
# 1-indexになるよう、形式的にnum[0] = 0とした
num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# dp[i] = i本のマッチで作れる最大の数
dp = [-1] * (N + 1)
dp[0] = 0

for i in range(N + 1):
    for a in A:
        # 遷移元がないならスキップ
        if dp[i] == -1:
            continue
        # 遷移先がないならスキップ
        elif i + num[a] > N:
            continue
        # 末尾にaをつける = 今の数字を10倍してaを足す
        else:
            dp[i + num[a]] = max(dp[i + num[a]], dp[i] * 10 + a)

# ちょうどN本使って作れる最大の数
print(dp[N])

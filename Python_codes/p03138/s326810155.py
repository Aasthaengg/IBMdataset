N,K = map(int, input().split())
A = [int(i) for i in input().split()]

# dp[i][j]: fの最大値
# i: 決定した桁数
# j: K以下確定フラグ
dp = [[-float("inf")] * 2 for _ in range(61)]

# 初期条件
dp[0][0] = 0

for i in range(60):
    one = 0 # 0の個数
    for a in A:
        if (a >> (59 - i)) & 1:
            one += 1
    zero = N - one # 1の個数

    for j in range(2):
        if dp[i][j] < 0:
            continue

        """ Xの(上から)i桁目を0にする -> 無条件"""
        dp[i+1][j | ((K >> (59 - i)) & 1)] = max(dp[i+1][j | ((K >> (59 - i)) & 1)], dp[i][j] + one * (1 << (59 - i)))

        """
        Xの(上から)i桁目を1にする場合の条件
        -> K以下未満が確定 or Kを超えない
        """
        if j or (K >> (59 - i)) & 1:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + zero * (1 << (59 - i)))

print(max(dp[60]))
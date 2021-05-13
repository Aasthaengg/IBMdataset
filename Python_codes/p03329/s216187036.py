N = int(input())
# dp[i] = 合計i円引き出すために必要な引出し回数
dp = [10**9 for _ in range(10 ** 5 + 1)]
dp[0] = 0

# 引き出せる金額のリスト
num = [1]
for i in range(1, 7):
    num.append(6**i)
for i in range(1, 6):
    num.append(9**i)

for i in range(10**5 + 1):
    for n in num:
        # 遷移元が存在する and 遷移先が存在する場合
        if dp[i] != -1 and i + n <= 10**5:
            dp[i + n] = min(dp[i + n], dp[i] + 1)

print(dp[N])

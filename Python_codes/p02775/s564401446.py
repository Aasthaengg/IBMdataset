# 通過の種類は10の100乗 + 1 種類
# 10の(10の100乗)乗の桁数は10の100乗桁 (1グーゴル)
# 10の6乗 = 1000000 (100万)
# 通過の方が圧倒的に大きい

s = input()[::-1]  # 与えられた数を下の桁から見る
length = len(s)
dp = [[0]*2 for _ in range(length+1)]  # j=1を更新するとき、お釣りの部分を格納していることになる（支払った1枚の紙幣は次のタイムステップで更新される）
for i in range(length):
    # 今見ている桁に関して、ちょうど支払うとき
    dp[i+1][0] = min(dp[i][0]+int(s[i]), dp[i][1]+int(s[i])+1)

    # 今見ている桁に関して、1つ大きい桁の紙幣を1枚使って支払う
    if i != 0:
        # ここで格納される値はお釣りの部分と考えることができる
        dp[i+1][1] = min(dp[i][0]+10-int(s[i]), dp[i][1]+(10-1)-int(s[i]))
    else:
        dp[i+1][1] = dp[i][0]+10-int(s[i])  # お釣りの部分のみが格納されている

print(min(dp[length][0], dp[length][1]+1))

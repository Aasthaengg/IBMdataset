from collections import defaultdict


N,K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
# 先頭からiビット目に1が立っている個数を数え上げる
for a in A:
    for i in range(50):
        if a & (1 << i):
            d[i] += 1
dp = [[-1 for _ in range(2)] for _ in range(51)]
dp[0][0] = 0

# 頭からi桁
for i in range(50):


    # 先頭からi番目の位置の数字
    if K & (1 << (50-i-1)):
        digit = 1
    else:
        digit = 0

    # i桁目に1を選んだ時
    use_1 = (N-d[50-i-1]) * (1 << (50-i-1))
    # i桁目に0を選んだ時
    use_0 = d[50-i-1] * (1 << (50-i-1))

    if K < (1 << (50-i-1)):
        use_1 = 0

    """
    i-1桁までがKより小さい場合、0,1どちらも選択可能
    dp[i][1] == -1 だとそれは起こりえない
    """
    if dp[i][1] != -1:
        dp[i+1][1] =  dp[i][1] + max(use_0, use_1)

    """
    i-1桁まで同じで、i桁目でKより小さくなる場合（Kのi桁目が1で0を選択）
    ここでmax(dp[i+1][1], ～)にしてあげないと、上で決めたものが上書きされてしまう
    """
    if dp[i][0] != -1:
        if digit == 1:
            dp[i+1][1] = max(dp[i+1][1], dp[i][0] + use_0)

    """
    i-1桁まで同じで、i桁目でKとまた一致する場合

    """
    if dp[i][0] != -1:
        if digit == 1:
            dp[i+1][0] = dp[i][0] + use_1
        else:
            dp[i+1][0] = dp[i][0] + use_0

print(max(dp[-1]))

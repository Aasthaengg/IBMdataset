
from collections import defaultdict



N,K = map(int, input().split())
A = list(map(int, input().split()))

"""
・K以下の非負整数の範囲で〜：桁DP感ある
・XORをとる：桁ごとに確認できる
・Xを選んで、f = X xor A1 + X xor A2 + ... + X xor AN
　 -> それぞれのAと毎回 xor 取るのではなく、桁ごとに xor を取ることができる　←　超重要のはず
　 -> A1 ~ AN の各桁（2進数の時の）に1が立っているのが何個あるか数えておく


遷移
dp[i][1] -> dp[i+1][1] : i-1桁目まででK未満が確定していれば、i桁目に1,0どちらを選んでもK未満
dp[i][0] -> dp[i+1][1]  : i-1桁目まででKと一致している場合、Kのi桁目が1なら、Xで0を選べば遷移できる
dp[i][0] -> dp[i+1][0]  : i桁目まで一致させる場合
"""

d = defaultdict(int)
for a in A:
    for i in range(45):
        if a & (1 << i):
            d[i] += 1

# dp[i+1][j] : Xをi桁目まで決めた時に、Kのi桁目までと厳密に一致するか（j=1でK未満）しないかの場合について、fの最大値
dp = [[-1 for _ in range(2)] for _ in range(45+1)]
# 初期化（何も見てない時のfの最大は0）
dp[0][0] = 0

for i in range(45):

    # Kの左からi番目に1が立ってるかどうか
    if K & (1 << (45 - 1 - i)):
        is_one = True
    else:
        is_one = False

    # Xの左からi桁目に1,0を設定した時にfが増加する量
    p0 = (2**(45-1-i)) * d[45-1-i]
    p1 = (2**(45-1-i)) * (N - d[45-1-i])

    # dp[i][1] -> dp[i+1][1] はXのi桁目に1,0を使えるから、より多い方を採用
    if dp[i][1] != -1:
        dp[i+1][1] = dp[i][1] + max(p1, p0)

    # dp[i][0] -> dp[i+1][1] はKのi桁目が1なら可能
    if dp[i][0] != -1:
        if is_one:
            dp[i+1][1] = max(dp[i+1][1], dp[i][0] + p0)
    
    # dp[i][0] -> dp[i+1][0] 
    if dp[i][0] != -1:
        if is_one:
            dp[i+1][0] = dp[i][0] + p1
        else:
            dp[i+1][0] = dp[i][0] + p0
    


print(max(dp[-1]))
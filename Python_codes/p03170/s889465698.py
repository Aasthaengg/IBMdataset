N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# dp[i]: 残りがi個の状態で先手が勝つかどうか
dp = [0 for _ in range(K+1)]

# dp[i] = 0: 残りi個で先手が負ける
# dp[i] = 1: 残りi個で先手が勝つ
# dp[i] = -1: 残りi個でも不明
  
for i in range(K + 1):
    # 遷移先: i-aで、そのとき手番は後手
    # どのi-aも1 = 後手がかならず勝つ = 負け
    # 1つでも0がある = 1つでも勝ち筋がある = (その手を打てば)勝ち
    # どのi-aにも遷移できない = 打てない = 負け
    for a in A:
        # 遷移先が存在し、かつそれが勝ち筋
        if i - a >= 0 and not dp[i - a]:
            dp[i] = 1
            break

if dp[K]:
    print('First')
else:
    print('Second')
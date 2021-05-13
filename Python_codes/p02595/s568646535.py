# NとDを定義
N, D = map(int, input().split())

# 原点からの距離がD以下となる点の個数を格納する変数の定義
dist_count = 0

# 原点からの距離がD以下の点の個数を評価
for i in range(N):
    # 座標の入力を定義
    x, y = map(int, input().split())
    # 原点からの距離がD以下となるか判定
    if x**2 + y**2 <= D**2:
        dist_count += 1

# 結果の出力
print(dist_count)
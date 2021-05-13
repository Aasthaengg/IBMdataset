# A - Sandglass2

# X 秒 図れる砂時計がある
# 上のパーツに X[g] 砂がある。　1秒に1[g]砂が落ちる。

# t 秒後に上のパーツに残っている砂は何[g]？

# X t を標準入力から得る
X, t = map(int, input().split())
# print(X, t)

# t <= X の時 X - t
# それ以外は、0 を代入
if t <= X:
    answer = X - t
else:
    answer = 0

# 結果を出力
print(answer)

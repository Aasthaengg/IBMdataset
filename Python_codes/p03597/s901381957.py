# N × N のマス目があります。
# このマス目の各マスを白色または黒色に塗ることにしました
# (すべてのマスをどちらか片方の色に塗ります)。
#
# ちょうど Aマスを白色に塗るとき、
# 黒色に塗ることになるマスはいくつあるでしょうか。

# 制約
# 1 ≦ N ≦ 100
# 0 ≦ A ≦ Nの2乗

# 標準入力から N, A の値を取得する
n = int(input())
a = int(input())

# 計算結果を出力する
result = (n * n) - a

print(result)

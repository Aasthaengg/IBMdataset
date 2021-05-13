# A - Bichrome Cells

# N * N のマス目がある。
# このマス目の各マスを白色または黒色に塗ることにしました (すべてのマスをどちらか片方の色に塗ります)
# ちょうど  A マスを白色に塗るとき、黒色に塗ることになるマスはいくつあるでしょうか。

# 黒色に塗ることになるマスの個数を出力

# 標準入力 N
N = int(input())

# 標準入力 A
A = int(input())
# print(N, A)

# マス数を計算
square_num = N * N
# print(square_num)

# 黒色に塗るマスの量を計算
answer = square_num - A

# 結果を出力
print(answer)

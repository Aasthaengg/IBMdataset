# 1軒のホテルがあります。 このホテルの宿泊費は、次のようになっています。
# ・最初の K泊までは、1泊あたり X円
# ・K + 1 目以降は、1泊あたり Y円
# 高橋君は、このホテルに N泊連続で宿泊することにしました。
# 高橋君の宿泊費は合計で何円になるか求めてください。

# 制約
# 1 ≤ N, K ≤ 10000
# 1 ≤ Y < X ≤ 10000
# N, K, X, Y はいずれも整数である

# 標準入力から、N, K, X, Yを取得する
input_n = int(input())
input_k = int(input())
input_x = int(input())
input_y = int(input())

# 宿泊費を計算して出力する
result = 0

for i in range(input_n):
    if i < input_k:
        result += input_x
    else:
        result += input_y

print(result)
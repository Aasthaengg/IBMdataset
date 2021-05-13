# A - 高橋君とホテルイージー

# 1  軒のホテルがあります。 このホテルの宿泊費は、次のようになっています。

# 最初の K 泊までは、1 泊あたり X 円
# K+1 泊目以降は、1 泊あたり Y 円

# このホテルに N 泊連続で宿泊する と 宿泊費は合計で何円になるか

# N 宿泊数　を標準入力から得る
N = int(input())
# K 最初の拍数　を標準入力から得る
K = int(input())
# X K日間の料金  を標準入力から得る
X = int(input())
# Y K+1~Nまでの料金 を標準入力から得る
Y = int(input())
# print(N, K, X, Y)

# K 泊までの料金を計算
# K * X
first_charge = K * X
# print(first_charge)

# K + 1 ~ N までの料金を計算
# (N - K) * Y
second_charge = (N - K) * Y
# print(second_charge)

# 合算
# K >= N の場合は、N * X 円
if K >= N:
    answer = N * X
else:
    answer = first_charge + second_charge

# 結果を出力
print(answer)

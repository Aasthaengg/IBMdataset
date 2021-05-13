# 入力
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# 処理
if N - K >= 1:
    print(K * X + (N - K) * Y)
else:
    print(N * X)
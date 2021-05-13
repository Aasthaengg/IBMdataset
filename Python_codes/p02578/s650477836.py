# cording:utf-8

# Nの入力
N = int(input())

# 要素数Nのリストを作成
N_i = [0] * N

# N個の整数の入力
N_i = list(map(int, input().split()))

# 踏み台高さ合計Sumを定義
Sum = 0

# N回の繰り返し
for i in range(1, N):
    # Sum_iを初期化
    Sum_i = 0

    # 直前の人の高さが自分より高ければ
    if N_i[i-1] > N_i[i]:
        # 仮のSum_iに踏み台の高さを代入
        Sum_i = N_i[i-1] - N_i[i]
        # N_iに上書き
        N_i[i] = N_i[i] + Sum_i
        # 合計値を算出
        Sum = Sum + Sum_i

print(Sum)

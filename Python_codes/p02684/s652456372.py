import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二次元配列作成
dv = []
for _ in range(int(math.log2(K)) + 1):
    l = [0] * N
    dv.append(l)

# dv[0][0:N]を初期化。1回目にいるところ
dv[0] = [a-1 for a in A]

# ダブリングで表を構築。2^n回目にいるところを埋める
for k in range(1, int(math.log2(K)) + 1):
    for n in range(N):
        dv[k][n] = dv[k - 1][dv[k - 1][n]]

# bitの立っている位置のみを取得
a = []
for i in range(int(math.log2(K)) + 1):
    if K >> i & 1:
        a.append(i)

now = 0
for i in a:
    now = dv[i][now]
print(now + 1)

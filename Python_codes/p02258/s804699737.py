import math

N = int(input())
R = [int(input().strip()) for _ in range(N)]

maxv = -math.inf
minv = R[0]
for i in range(1, N):

    tmp_maxv = R[i] - minv # 差額をセットする
    # 現在の最大差額と差額の大きい方を最大差額にする
    if maxv < tmp_maxv:
        maxv = tmp_maxv

    # 現在値が最小なら、最小値を更新する
    if R[i] < minv:
        minv = R[i]

print(maxv)

# -*- coding: utf-8 -*-

N, M = map(int, input().split())
ab = []
cd = []

# 学生の位置の取得
for i in range(N):
    tmp = list(map(int, input().split()))
    ab.append(tmp)

# チェックポイントの位置の取得
for i in range(M):
    tmp = list(map(int, input().split()))
    cd.append(tmp)


# 変数初期化
tmp_d = 0

# 学生を1人ずつ評価
for i in range(N):
    # 最小番号、最小距離の初期化
    min_d = 2 * (10 ** 8)
    min = 1
    for j in range(M):
        # マンハッタン距離の算出
        tmp_d = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if min_d > tmp_d:
            min_d = tmp_d
            min = j + 1
            #print('min', min)
    print(min)
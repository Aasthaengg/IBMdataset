N, C = map(int, input().split())
Xi = [list(map(int, input().split())) for _ in range(N)]

#両端に(0,0)があると考えると楽なので追加
Xi.insert(0, [0, 0])
Xi.append([C, 0])

# 真上に0があると考える。下から⇢にいくか←にいくかで区別
#右方向に進んだときの累積Caloryと累積max
total = 0
R_max = [0 for i in range(N + 2)]
for i in range(1, N + 1):
    total += Xi[i][1] - (Xi[i][0] - Xi[i - 1][0])
    R_max[i] = max(total, R_max[i - 1])

#右方向に進んだときの累積max
total = 0
L_max = [0 for i in range(N + 2)]
for i in range(N, 0, -1):
    total += Xi[i][1] - (Xi[i + 1][0] - Xi[i][0])
    L_max[i] = max(total, L_max[i + 1])

max_value = 0
for i in range(0, N + 1):
    i2 = N - i - 1
    #右方向にとにかくすすむ
    cal = R_max[i] + L_max[i + 1] - Xi[i][0]
    max_value = max(cal, max_value)

    #左にとにかくすすむ
    cal = R_max[i] + L_max[i + 1] - (C - Xi[i + 1][0])
    max_value = max(cal, max_value)
print(max_value)
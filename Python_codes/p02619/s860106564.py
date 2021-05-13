import numpy as np

d = int(input())    # Day
C = list(map(int, input().split()))  # 満足度の減少係数
S = []  # 各日にち、各タイプの満足度
T = []  # d日目の開催タイプ
L = [0] * 26    # 各コンテストが開催された最後の日付

for _ in range(d):
    S.append(list(map(int, input().split())))  # Si,d type_iをdayDに開いた時の満足度 [5, 26]

for _ in range(d):
    T.append(int(input()))

# print("d:", d)
# print("C:", C)
# print("S:", S)
# print("T:", T)

sat = 0
S = np.array(S)

for i in range(d):
    con_type = T[i]
    # print("開催するコンテストタイプ：", con_type)
    complain = 0
    L[con_type - 1] = i + 1     # 最終開催日の更新
    for j in range(26):
        # print("{} + {} * ({} - {})".format(complain, C[j], i+1, L[j]))
        complain = complain + C[j] * (i + 1 - L[j])

    # print("complain:", complain)
    # print("S:", S[i][con_type - 1])
    # print("satの計算: {} + {} - {}".format(sat, S[i][con_type - 1], complain ))

    sat = sat + S[i][con_type - 1] - complain

    print(sat)


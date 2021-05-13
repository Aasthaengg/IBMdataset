# ['表面', '南面', '東面', '西面', '北面', '裏面']
dice1 = [int(d) for d in input().split()]
Q = int(input())

R1 = [
    [0, 1, 2, 3, 4, 5], # 移動なし
    [3, 1, 0, 5, 4, 2], # 東へ1
    [2, 1, 5, 0, 4, 3], # 西へ1
    [4, 0, 2, 3, 5, 1], # 南へ1
    [1, 5, 2, 3, 0, 4], # 北へ1
    [5, 4, 2, 3, 1, 0]  # 北へ2
]

R2 = [0, 3, 1, 4, 2, 5] # 水平回り1

for _ in range(Q):
    F, S = map(int, input().split())
    for r1 in R1:
        dice2 = [dice1[i] for i in r1]
        for _ in range(4):
            dice2 = [dice2[i] for i in R2]
            if dice2[0] == F and dice2[1] == S:
                print(dice2[2])

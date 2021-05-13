s = input()
x, y = map(int, input().split())

# Tで区切り、各Tの前にFが何文字あるか数える
steps = []
cnt = 0
for i in range(len(s)):
    if s[i] == "F":
        cnt += 1
    elif s[i] == "T":
        steps.append(cnt)
        cnt = 0
# 最後のブロックについて
if cnt > 0:
    steps.append(cnt)
AX = steps[0::2]
AY = steps[1::2]

# X軸方向の最大値
max_X = sum(AX)
# dpX[i][j] = X軸方向の移動をi回行って、jに到達できるか
# j = 0, 1, ..., 2*max_X だが、実際のX座標は -max_X, ..., 0, ..., max_X
# 原点(x=0)は、j = max_Xに相当する
dpX = [[0 for _ in range(2 * max_X + 1)] for _ in range(len(AX) + 1)]
dpX[0][max_X] = 1
# 最初に右へ移動する場合
if s[0] == "F":
    dpX[1][max_X + AX[0]] = 1
    for i in range(1, len(AX)):
        for j in range(2 * max_X + 1):
            if dpX[i][j] == 1:
                # +X方向に移動
                if j + AX[i] <= 2 * max_X:
                    dpX[i + 1][j + AX[i]] = 1
                # -X方向に移動
                if 0 <= j - AX[i]:
                    dpX[i + 1][j - AX[i]] = 1
# 最初に回転する場合
else:
    for i in range(len(AX)):
        for j in range(2 * max_X + 1):
            if dpX[i][j] == 1:
                # +X方向に移動
                if j + AX[i] <= 2 * max_X:
                    dpX[i + 1][j + AX[i]] = 1
                # -X方向に移動
                if 0 <= j - AX[i]:
                    dpX[i + 1][j - AX[i]] = 1
# Y軸方向の最大値
max_Y = sum(AY)
# dpY[i][j] = Y軸方向の移動をi回行って、jに到達できるか
# j = 0, 1, ..., 2*max_Y だが、実際のY座標は -max_Y, ..., 0, ..., max_Y
# 原点(y=0)は、j = max_Yに相当する
dpY = [[0 for _ in range(2 * max_Y + 1)] for _ in range(len(AY) + 1)]
dpY[0][max_Y] = 1
for i in range(len(AY)):
    for j in range(2 * max_Y + 1):
        if dpY[i][j] == 1:
            # +Y方向に移動
            if j + AY[i] <= 2 * max_Y:
                dpY[i + 1][j + AY[i]] = 1
            # -Y方向に移動
            if 0 <= j - AY[i]:
                dpY[i + 1][j - AY[i]] = 1

if -max_X <= x <= max_X and -max_Y <= y <= max_Y:
    if dpX[-1][x + max_X] == 1 and dpY[-1][y + max_Y] == 1:
        print("Yes")
        exit()
print("No")

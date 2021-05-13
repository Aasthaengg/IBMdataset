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

step_X = steps[0::2]
step_Y = steps[1::2]

# X軸方向の最大値
max_X = sum(step_X)
# dp_X[i][j] = X軸方向の移動をi回行って、jに到達できるか
# j = 0, 1, ..., 2*max_X だが、実際のX座標は -max_X, ..., 0, ..., max_X
# 原点(x=0)は、j = max_Xに相当する
dp_X = [[0 for _ in range(2 * max_X + 1)] for _ in range(len(step_X) + 1)]
dp_X[0][max_X] = 1
# 最初に右へ移動する場合
if s[0] == "F":
    dp_X[1][max_X + step_X[0]] = 1
    for i in range(1, len(step_X)):
        for j in range(2 * max_X + 1):
            if dp_X[i][j] == 1:
                # +X方向に移動
                if j + step_X[i] <= 2 * max_X:
                    dp_X[i + 1][j + step_X[i]] = 1
                # -X方向に移動
                if 0 <= j - step_X[i]:
                    dp_X[i + 1][j - step_X[i]] = 1
# 最初に回転する場合
else:
    for i in range(len(step_X)):
        for j in range(2 * max_X + 1):
            if dp_X[i][j] == 1:
                # +X方向に移動
                if j + step_X[i] <= 2 * max_X:
                    dp_X[i + 1][j + step_X[i]] = 1
                # -X方向に移動
                if 0 <= j - step_X[i]:
                    dp_X[i + 1][j - step_X[i]] = 1

# Y軸方向の最大値
max_Y = sum(step_Y)
# dp_Y[i][j] = Y軸方向の移動をi回行って、jに到達できるか
# j = 0, 1, ..., 2*max_Y だが、実際のY座標は -max_Y, ..., 0, ..., max_Y
# 原点(y=0)は、j = max_Yに相当する
dp_Y = [[0 for _ in range(2 * max_Y + 1)] for _ in range(len(step_Y) + 1)]
dp_Y[0][max_Y] = 1
for i in range(len(step_Y)):
    for j in range(2 * max_Y + 1):
        if dp_Y[i][j] == 1:
            # +Y方向に移動
            if j + step_Y[i] <= 2 * max_Y:
                dp_Y[i + 1][j + step_Y[i]] = 1
            # -Y方向に移動
            if 0 <= j - step_Y[i]:
                dp_Y[i + 1][j - step_Y[i]] = 1

if -max_X <= x <= max_X and -max_Y <= y <= max_Y:
    if dp_X[-1][x + max_X] == 1 and dp_Y[-1][y + max_Y] == 1:
        print("Yes")
        exit()
print("No")

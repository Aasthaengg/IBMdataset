N = int(input())

# 現時点でのパラメータ
pt = 0
px = 0
py = 0

for i in range(N):
    t, x, y = map(int, input().split())

    time = abs(t - pt)
    # いわゆるマンハッタン距離
    dist = abs(x - px) + abs(y - py)

    if dist > time:
        print("No")
        exit()

    # x+yの偶奇は毎秒変わる
    # timeとdistの偶奇は一致する
    if time % 2 != dist % 2:
        print("No")
        exit()

    pt, px, py = t, x, y

print("Yes")
W, H, x, y = map(int, input().split())

# 大きくない方とかって書いてあるけど、別にイコールの場合でもいいんかい！
# 中心の座標を求める
centerX = (W / 2)
centerY = (H / 2)

if ((x, y) == (centerX, centerY)):
    print((W * H) / 2, 1)

else:
    print(W * H / 2, 0)

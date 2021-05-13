w, h, x, y = map(int, input().split())

# 面積の最大値は常に長方形の半分
# (x, y)がど真ん中の時だけ縦にも横にも切れる
ans = 0
if ((w / 2) == x) & ((h / 2) == y):
    ans = 1

print(w * h / 2, ans)
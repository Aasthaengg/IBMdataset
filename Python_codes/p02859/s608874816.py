# mathモジュールをインポート
import math

# 円の面積を求める関数
def circle(r):
  return r*r*math.pi

r = input().rstrip()
r = int(r)

# 円の面積
r_circle = circle(r)

# 半径1の円の面積
one_r_circle = circle(1)

ans = round(r_circle / one_r_circle)
print(ans)

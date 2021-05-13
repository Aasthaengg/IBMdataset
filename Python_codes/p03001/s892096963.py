# 点(x, y)から長方形の中心を通る直線を引くと面積を半分にすることができ、分割された小さい方の面積が最大となる
# 点(x, y)が長方形の中心と一致する場合、直線は複数存在する

w, h, x, y = map(int, input().split())

s = w * h
s_min = s / 2

# 中心
a = w / 2
b = h / 2

divide = 0

if x == a and y == b:
    divide = 1
    print(s_min, divide)
else:
    print(s_min, divide)
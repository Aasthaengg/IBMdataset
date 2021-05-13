# 台形の面積
# 台形の計算が、float型で計算されるので、最後は整数で出力する。

upper_floor = int(input())
bottom_floor = int(input())
height = int(input())

trapezoid = (upper_floor + bottom_floor) * height / 2
print(int(trapezoid))
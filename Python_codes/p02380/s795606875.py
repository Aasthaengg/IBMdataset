import math

a, b, C = map(int, input().split())

c = math.sqrt(a**2 + b**2 - (2 * a * b* math.cos(math.radians(C))))
L = a + b + c # 周の長さ
s = L / 2 # 周の長さの半分
S = math.sqrt(s * (s - a) * (s - b) * (s - c))# 面積
h = (2 * S) / a
print("{}\n{}\n{}".format(S, L, h))

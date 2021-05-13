# https://atcoder.jp/contests/abc144/tasks/abc144_d
from math import radians, sin, cos, tan, degrees, atan
a, b, x = map(int, input().split())

# ans = a * b * (b * tan(radians(45))) / 2
# print(ans, tan(radians(45)))
# x = a * b * (b * tan(radians(ans))) / 2
# 2 * x / (a * b) = (b * tan(radians(ans)))
# 2 * x / (a * b) / b = tan(radians(ans))

if a * a * b / 2. <= x:
    ans = degrees(atan(2 * (a * a * b - x) / (a * a * a)))
else:
    ans = 90 - degrees(atan((2 * x) / (a * b * b)))
print(ans)
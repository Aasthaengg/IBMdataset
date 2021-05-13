from math import atan, pi
a, b, x = map(int, input().split())

if x > a * a * b / 2:
    h = 2 * x / (a * a) - b
    ans = atan((b - h) / a)
else:
    h = 2 * x / (a * b)
    ans = pi / 2 - atan(h/b)

ans *= 180 / pi
print("{:.12f}".format(ans))
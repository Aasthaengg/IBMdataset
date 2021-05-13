
from math import cos, pi

A, B, H, M = map(int, input().split())

t1 = 30 * H + M / 60 * 30
t2 = 6 * M
ans = A ** 2 + B ** 2 - 2 * A * B * cos(abs(t1 - t2) * pi / 180)
print(ans ** 0.5)

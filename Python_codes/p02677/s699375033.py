import math

A, B, H, M = map(int, input().split())

Minute_angle = (M / 60) * 2 * math.pi
Time_angle = (H + (M / 60)) * math.pi / 6
theta = Minute_angle - Time_angle
ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta))
print(ans)
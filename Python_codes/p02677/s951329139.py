import math

A, B, H, M = map(int, input().split())

theta_tansin = 360 * H / 12 + 30 * M / 60
theta_chosin = 360 * M / 60

theta = abs(theta_tansin - theta_chosin)
theta = min(theta, 360 - theta)
theta = math.radians(theta)

C = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta))

print(C)
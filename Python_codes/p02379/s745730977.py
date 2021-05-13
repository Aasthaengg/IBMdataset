import math

x1, y1, x2, y2 = list(map(float, input().split()))

exp_dist = abs(x1 - x2)**2 + abs(y1 - y2)**2

print(math.sqrt(exp_dist))
import math
a, b, t = map(int, input().split())
T = t + 0.5
times = math.floor(T / a)

print(times*b)
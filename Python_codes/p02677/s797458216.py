import math
A, B, H, M = map(int,input().split())
a = (((H + M / 60) * 2 * math.pi) / 12) - ((M * 2 * math.pi) / 60)
b = (A ** 2 + B ** 2 - 2 * A * B * math.cos(a)) ** 0.5
print(b)
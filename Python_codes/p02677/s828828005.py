import math
 
A, B, H, M = map(int, input().split())
 
m = (M / 60) * 2 * math.pi
t = (H + (M / 60)) * math.pi / 6
angle = m-t
res = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(angle))
print(res)
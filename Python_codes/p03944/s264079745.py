import sys
import numpy as np
# from decimal import Decimal
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

w, h, n = map(int, readline().split())
left = 0
right = w
up = h
down = 0

s = w * h
for i in range(n):
    x, y, a = map(int, readline().split())
    if (a == 1):
        left = max(x, left)
    elif (a == 2):
        right = min(x, right)
    elif (a == 3):
        down = max(y, down)
    else:
        up = min(y, up)

    if (right - left <= 0) or (up - down <= 0):
        print(0)
        exit()

ans = (right - left) * (up - down)
print(ans)

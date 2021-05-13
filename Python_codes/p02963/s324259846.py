import math

s = int(input())

mod = 10**9

if s <= mod:
    print(0, 0, 0, 1, s, 0)
else:
    x1, x2 = mod, 1
    y2 = math.ceil(s / mod)
    y1 = y2 * mod - s
    print(0, 0, x1, x2, y1, y2)
from math import atan
from math import degrees

a, b, x = [int(x) for x in input().split()]

volume = a * a * b
volume_per = x / volume

if volume_per >= 0.5:
    up = b * (1 - volume_per)
    down = a / 2
else:
    up = b
    down = 2 * a * volume_per

print(degrees(atan(up/down)))

import math

x, y = map(int, input().split())
ave = (x + y) / 2
ave = math.ceil(ave)
print(ave)
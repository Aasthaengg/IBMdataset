import math
x = int(input())
if (x >= 100) & (math.ceil(((x % 100) / 5)) <= x // 100):
    print(1)
else:
    print(0)
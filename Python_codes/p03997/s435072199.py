import math
a, b, h = [int(input()) for i in range(3)]

area = (a + b) * h / 2
print(math.floor(area))
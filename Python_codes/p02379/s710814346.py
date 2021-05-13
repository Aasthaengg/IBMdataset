import math
x1, y1, x2, y2 = map(float, input().split())

r = (x1 - x2) ** 2 + (y1 - y2)**2
r = math.sqrt(r)
print(format(r, '.8f'))

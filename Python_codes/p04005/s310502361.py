import math
a, b, c = map(int, input().split())
l = [a, b, c]
l.sort()
x = l[2]
print(math.ceil(x / 2) * l[0] * l[1] - math.floor(x / 2) * l[0] * l[1])

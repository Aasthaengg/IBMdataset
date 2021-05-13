import math
l = input().split()
x1 = float(l[0])
y1 = float(l[1])
x2 = float(l[2])
y2 = float(l[3])

a = pow((x2 - x1), 2) + pow((y2 - y1), 2)
ans = math.sqrt(a)
print(ans)
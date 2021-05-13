import math

buf = input().split()

x1 = float(buf[0])
y1 = float(buf[1])
x2 = float(buf[2])
y2 = float(buf[3])

dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(dis)



import math
x1, y1, x2, y2 = map(int, input().split())
x2 -= x1
y2 -= y1
if x2 != 0:
    theta = math.atan2(y2,x2)
else:
    if y2 > 0:
        theta = math.pi / 2
    else:
        theta = 3 * math.pi / 2
if y2 == 0:
    if x2 < 0:
        theta = math.pi
    else:
        theta = 0

if theta < 0:
    theta += 2 * math.pi
#theta = theta % (2 * math.pi)

l = math.sqrt(x2**2 + y2**2)

x3 = math.cos(theta+math.radians(45))*l*math.sqrt(2)+x1
y3 = math.sin(theta+math.radians(45))*l*math.sqrt(2)+y1

x4 = math.cos(theta+math.radians(90))*l+x1
y4 = math.sin(theta+math.radians(90))*l+y1
print(round(x3), round(y3), round(x4), round(y4))
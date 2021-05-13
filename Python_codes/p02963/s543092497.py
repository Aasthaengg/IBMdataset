import math
s = int(input())
x1 = y1 = 0
x2 = y3 = math.ceil(s**0.5)
x3 = y2 = 0
diff = x2*y3 - s
for i in range(int(diff**0.5), 0, -1):
    if diff % i == 0:
        x3 = i
        y2 = diff // i
print(x1,y1,x2,y2,x3,y3)

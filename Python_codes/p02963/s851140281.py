import math
s = int(input())

x1 = 10**9
y2 = math.ceil(s/10**9)
x2 = 1
y1 = x1*y2 - s

print(0,0,x1,y1,x2,y2)
import math
x1,y1,x2,y2 = map(float,input().split(" "))
yoko = x2 - x1
tate = y2 - y1
print(math.sqrt(yoko**2+tate**2))
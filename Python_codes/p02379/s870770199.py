import math
x1,y1,x2,y2 = map(float,raw_input().split())
x = x2-x1
y = y2-y1
print math.sqrt(math.pow(x,2)+math.pow(y,2))
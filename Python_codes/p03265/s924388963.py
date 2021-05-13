x1,y1,x2,y2 = map(int,input().split())


c = x2 - x1
d = y2 - y1
x3 = x2 - d
y3 = y2 + c
x4 = x3 - c
y4 = y3 - d
print(x3,y3,x4,y4)
x1,y1,x2,y2 = map(int,input().split())
 
x = x2 - x1
y = y1 - y2
 
x3 = x2 + y
y3 = y2 + x
x4 = x3 - x
y4 = y3 + y

print(x3,y3,x4,y4)

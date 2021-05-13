x1,y1,x2,y2 = map(int,input().split())
difx = x2 - x1
dify = y2 - y1
x3 = x2 - dify
y3 = y2 + difx
x4 = x1 - dify
y4 = y1 + difx
print(x3,y3,x4,y4)
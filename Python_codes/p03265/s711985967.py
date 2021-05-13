x1,y1,x2,y2 = map(int,input().split())
difx = x2-x1
dify = y2-y1
x3 = x2 - dify
y3 = y2 + difx
x4 = x3 - difx
y4 = y3 - dify
print("{a} {b} {c} {d}".format(a=x3,b=y3,c=x4,d=y4))
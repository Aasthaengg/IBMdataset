x1,y1,x2,y2 = map(int,input().split())

delx12 = x2-x1
dely12 = y2-y1

x3 = x2-dely12
y3 = y2 +delx12
x4 = x3-delx12
y4 =y3-dely12

print(x3,y3,x4,y4)
x1,y1,x2,y2=map(int,input().split())
xdis=x2-x1
ydis=y2-y1
x3=x2-ydis
y3=y2+xdis
x4=x1-ydis
y4=y1+xdis
print(x3,y3,x4,y4)
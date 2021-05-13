x1,y1,x2,y2=map(int,input().split())
X=x1-x2
Y=y1-y2
x3,y3=x2+Y,y2-X
x4,y4=x3+X,y3+Y
print(x3,y3,x4,y4)
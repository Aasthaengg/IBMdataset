x1,y1,x2,y2=map(int,input().split())
h=y2-y1;w=x2-x1
x3=x2-h
y3=y2+w
x4=x3-w
y4=y3-h
print(x3,y3,x4,y4)
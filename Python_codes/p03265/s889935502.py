x1,y1,x2,y2=map(int,input().split())
x3,x4,y3,y4=0,0,0,0
a=x2-x1
b=y2-y1
x3=x2-b
y3=a+y2
x4=x3-a
y4=y3-b
print(x3,y3,x4,y4)
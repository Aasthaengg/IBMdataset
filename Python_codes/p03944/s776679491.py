w,h,n=map(int,input().split())
x1=0
x2=w
y1=0
y2=h

for i in range(n):
    x,y,a=map(int,input().split())
    if a==1:
        if x1<x:
            x1=x
    elif a==2:
        if x<x2:
            x2=x
    elif a==3:
        if y1<y:
            y1=y
    else:
        if y<y2:
            y2=y

if x2<=x1 or y2<=y1:
    print(0)
else:
    print((x2-x1)*(y2-y1))
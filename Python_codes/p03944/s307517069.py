w,h,n=map(int,input().split())
S=w*h
h1=0
w1=0
xmax=0
ymax=0
xmax_r=0
ymax_r=0



for i in range(n):
    x,y,a=map(int,input().split())
    if a==1:
        if xmax<x:
            xmax=x
    
    if a==2:
        if xmax_r<w-x:
            xmax_r=w-x
    
    if a==3:
        if ymax<y:
            ymax=y
    
    if a==4:
        if ymax_r<h-y:
            ymax_r=h-y

if (w-xmax-xmax_r)<=0 or (h-ymax-ymax_r)<=0:
    print("0")
else:
    print((w-xmax-xmax_r)*(h-ymax-ymax_r))
w,h,n=map(int,input().split())
lx=0
rx=w
sy=h
iy=0
for i in range(n):
    x,y,a=map(int,input().split())
    if a==1:
        lx=max(lx,x)
    elif a==2:
        rx=min(rx,x)
    elif a==3:
        iy=max(iy,y)
    else:
        sy=min(sy,y)
x=rx-lx
y=sy-iy
if x<0 or y<0:
    print(0)
    exit()
print(x*y)
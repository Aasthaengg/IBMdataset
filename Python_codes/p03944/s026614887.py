W,H,N = map(int,input().split())
xl = 0
xh = W
yl = 0
yh = H
for _ in range(N):
    x,y,a = map(int,input().split())
    if a==1:
        xl = max(xl,x)
    elif a==2:
        xh = min(xh,x)
    elif a==3:
        yl = max(yl,y)
    elif a==4:
        yh = min(yh,y)
dx = max(0,xh-xl)
dy = max(0,yh-yl)
print(dx*dy)
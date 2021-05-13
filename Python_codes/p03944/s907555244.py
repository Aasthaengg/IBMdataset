w,h,n = map(int,input().split())
xs = 0
ys = 0
xe = w
ye = h
for i in range(n):
    x,y,a = map(int,input().split())
    if a == 2:
        xe = min(xe,x)
    elif a == 1:
        xs = max(xs,x)
    elif a == 4:
        ye = min(ye,y)
    else:
        ys = max(ys,y)
if xs < xe and ys < ye:
    print(abs(xs-xe)*abs(ys-ye))
else:
    print(0)
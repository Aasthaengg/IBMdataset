w,h,n = map(int,input().split())
yu = h
yd = 0
xl = 0
xr = w
for i in range(n):
    x,y,a= map(int,input().split())
    if a == 1:
        xl = max(x,xl)
    elif a == 2:
        xr = min(x,xr)
    elif a == 3:
        yd = max(y,yd)
    elif a == 4:
        yu = min(y,yu)
    # print(xl,xr,yu,yd)
print(max(0,yu-yd)*max(0,xr-xl))                        
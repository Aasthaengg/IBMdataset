w,h,n = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
xl = 0
xr = w
yh = h
yr = 0
for i in range(n):
    if a[i][2] == 1:
        xl = max(xl,a[i][0])
    elif a[i][2] == 2:
        xr = min(xr,a[i][0])
    elif a[i][2] == 3:
        yr = max(yr,a[i][1])
    else:
        yh = min(yh,a[i][1])

x = xr - xl
y = yh - yr

print(0 if x < 0 or y < 0 else x*y)
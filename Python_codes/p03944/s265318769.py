w,h,n = map(int,input().split())
lists = [list(map(int,input().split())) for i in range(n)]
x1 = 0
x2 = w
y1 = 0
y2 = h
for x,y,a in lists:
    if a == 1:
        x1 = max(x1,x)
    elif a == 2:
        x2 = min(x2,x)
    elif a == 3:
        y1 = max(y1,y)
    elif a == 4:
        y2 = min(y2,y)
x = max(0,(x2 - x1))
y = max(0,(y2 - y1))
ans = max(0,x*y)
print(ans)
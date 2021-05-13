w,h,n = map(int,input().split())
c = [list(map(int,input().split())) for i in range(n)]
xmin = 0
xmax = w 
ymin = 0
ymax = h
for i in c:
    if i[2]==1:
        xmin = max(xmin,i[0])
    elif i[2]==2:
        xmax = min(xmax,i[0])
    elif i[2]==3:
        ymin = max(ymin,i[1])
    elif i[2]==4:
        ymax = min(ymax,i[1])
if xmax>xmin and ymax>ymin:
    print((xmax-xmin)*(ymax-ymin))
else:
    print(0)
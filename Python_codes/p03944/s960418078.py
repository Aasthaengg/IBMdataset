W, H, N = map(int, input().split())

lstx = [[0], [W]]
lsty = [[0], [H]]

for i in range(N):
    x, y, a = map(int, input().split())
    if a==1 or a==2:
        lstx[a-1].append(x)
    else:
        lsty[a-3].append(y)

xmax = max(lstx[0])
xmin = min(lstx[1])
ymax = max(lsty[0])
ymin = min(lsty[1])

if xmax <= xmin and ymax <= ymin:
    print((xmax-xmin)*(ymax-ymin))
else: print(0)


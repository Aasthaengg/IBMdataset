w, h, n = map(int, input().split())

maxx = w
minx = 0
maxy = h
miny = 0

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        minx = max(minx, x)
    elif a == 2:
        maxx = min(maxx, x)
    elif a == 3:
        miny = max(miny, y)
    else:
        maxy = min(maxy, y)

ans = (maxx-minx)*(maxy-miny)
if minx > maxx or miny > maxy:
    print(0)
else:
    print(ans)

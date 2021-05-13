x1, y1, x2, y2 = map(int, input().split())

xdiff = x2 - x1
ydiff = y2 - y1

x3 = x2 - ydiff
x4 = x1 - ydiff
y3 = y2 + xdiff
y4 = y1 + xdiff

print(x3, y3, x4, y4)
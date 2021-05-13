x1, y1, x2, y2 = map(int, input().split())
xdiff = x2 - x1
ydiff = y2 - y1
print(x2 - ydiff, y2 + xdiff, x1 - ydiff, y1 + xdiff)
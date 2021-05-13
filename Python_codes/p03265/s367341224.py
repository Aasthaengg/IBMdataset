x1, y1, x2, y2 = map(int, input().split())

xDiff, yDiff = x1 - x2, y1 - y2

print(x2+yDiff, y2-xDiff, x1+yDiff, y1-xDiff)
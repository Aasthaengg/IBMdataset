x1, y1, x2, y2 = map(int, input().split())
dx1, dy1 = x2 - x1, y2 - y1
dx2, dy2 = -dy1, dx1
x3, y3 = x2 + dx2, y2 + dy2
x4, y4 = x3 - dx1, y3 - dy1
print(x3, y3, x4, y4)
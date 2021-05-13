x1, y1, x2, y2 = map(int, input().split())
dx = x2 - x1
dy = y2 - y1
xx3 = (x2 - dy, y2 + dx)
xx4 = (x1 - dy, y1 + dx)
print(*xx3, *xx4)

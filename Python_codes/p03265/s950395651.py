x1, y1, x2, y2 = list(map(int, input().split()))
dx, dy = x1 - x2 , y2 - y1
print(x2 - dy, y2 -dx, x1 - dy, y1 -dx)
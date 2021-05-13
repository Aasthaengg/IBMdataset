x1, y1, x2, y2 = map(int, input().split())

x = x2 - x1
y = y2 - y1
dx = y
dy = x

x3 = x2-dx
y3 = y2+dy
x4 = x1-dx
y4 = y1+dy

print(x3, y3, x4, y4)

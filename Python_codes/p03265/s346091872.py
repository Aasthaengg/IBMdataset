x1, y1, x2, y2 = map(int, input().split())

dx12 = x2 - x1
dy12 = y2 - y1
dx23 = -dy12
dy23 = dx12
dx34 = -dy23
dy34 = dx23

x3 = x2 + dx23
y3 = y2 + dy23
x4 = x3 + dx34
y4 = y3 + dy34

print('{} {} {} {}'.format(x3, y3, x4, y4))

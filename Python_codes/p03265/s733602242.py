x1, y1, x2, y2 = list(map(int, input().split()))

vx = x2 - x1
vy = y2 - y1

x3 = x2 - vy
y3 = y2 + vx
x4 = x1 - vy
y4 = y1 + vx

print(x3, y3, x4, y4)
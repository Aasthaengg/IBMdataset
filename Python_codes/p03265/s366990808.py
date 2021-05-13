x1, y1, x2, y2 = map(int, input().split())

delta_x21 = x2 - x1
delta_y21 = y2 - y1
delta_x32 = -delta_y21
delta_y32 = delta_x21
x3 = x2 + delta_x32
y3 = y2 + delta_y32
x4 = x3 - delta_x21
y4 = y3 - delta_y21

print(x3, y3, x4, y4)
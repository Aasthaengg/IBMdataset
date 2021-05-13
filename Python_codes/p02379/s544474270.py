
x1, y1, x2, y2 = (float(i) for i in input().split())
x_range = x2 - x1
y_range = y2 - y1

distance = pow(pow(x_range, 2) + pow(y_range, 2), 1/2)

print(distance)
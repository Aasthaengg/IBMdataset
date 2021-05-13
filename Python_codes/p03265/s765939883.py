x1, y1, x2, y2 = map(int, input().split())
x_distance = x2 - x1
y_distance = y2 - y1
print("{} {} {} {}".format(x2 - y_distance, y2 + x_distance, x1 - y_distance, y1 + x_distance))
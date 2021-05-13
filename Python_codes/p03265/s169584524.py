x1, y1, x2, y2 = map(int, input().split())

sa_x = x2 - x1
sa_y = y2 - y1

print(x2 - sa_y, y2 + sa_x, x1 - sa_y, y1 + sa_x)
x1, y1, x2, y2 = map(int, input().split())
l = y1 - y2
m = x1 - x2
print("{} {} {} {}".format(x2 + l, y2 - m, x1 + l, y1 - m))
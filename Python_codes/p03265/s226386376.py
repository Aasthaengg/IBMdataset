x1, y1, x2, y2 = map(int, input().split())

x_ = x2-x1
y_ = y2-y1

x_l = abs(x_)
y_l = abs(y_)

if x_ > 0 and y_ >= 0:
    x3 = x2 - y_l
    y3 = y2 + x_l
    x4 = x3 - x_l
    y4 = y3 - y_l

elif x_ < 0 and y_ <= 0:
    x3 = x2 + y_l
    y3 = y2 - x_l
    x4 = x3 + x_l
    y4 = y3 + y_l

elif x_ <= 0 and y_ > 0:
    x3 = x2 - y_l
    y3 = y2 - x_l
    x4 = x3 + x_l
    y4 = y3 - y_l

elif x_ >= 0 and y_ < 0:
    x3 = x2 + y_l
    y3 = y2 + x_l
    x4 = x3 - x_l
    y4 = y3 + y_l


print(int(x3), int(y3), int(x4), int(y4))

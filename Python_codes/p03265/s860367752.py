x1, y1, x2, y2 = map(int, input().split())

xv_12, yv_12 = x2-x1, y2-y1
xv_23, yv_23 = yv_12*-1, xv_12
xv_34, yv_34 = yv_23*-1, xv_23

x3, y3 = x2+xv_23, y2+yv_23
x4, y4 = x3+xv_34, y3+yv_34

print(x3, y3, x4, y4)


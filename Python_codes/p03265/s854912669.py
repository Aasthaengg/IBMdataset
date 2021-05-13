xy = list(map(int, input().split()))
x = list(xy[i] for i in range(0, 4, 2))
y = list(xy[i] for i in range(1, 4, 2))
x1 = x[1]-x[0]
y1 = y[1]-y[0]
print(x[1]-y1, y[1]+x1, x[0]-y1, y[0]+x1)


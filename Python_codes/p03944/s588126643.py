W, H, N = map(int, input().split())
xs = [0, W]
ys = [0, H]
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1 and x > xs[0]:
        xs[0] = x
    elif a == 2 and x < xs[1]:
        xs[1] = x
    elif a == 3 and y > ys[0]:
        ys[0] = y
    elif a == 4 and y < ys[1]:
        ys[1] = y
    else:
        pass
x_len = xs[1] - xs[0] if xs[1] > xs[0] else 0
y_len = ys[1] - ys[0] if ys[1] > ys[0] else 0
print(x_len * y_len)

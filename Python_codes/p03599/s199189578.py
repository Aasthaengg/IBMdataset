a, b, c, d, e, f = map(int, input().split())
xas = [i *100*a for i in range(f // a // 100 + 1)]
xbs = [i *100*b for i in range(f // b // 100 + 1)]
xs = {(i+j) for i in xas for j in xbs if i+j <= f}
yc = [i*c for i in range(f//c+1)]
yd = [i*d for i in range(f//d+1)]
ys = {(i+j) for i in yc for j in yd if i + j <= f}
x, y, m = 0, 0, 0
for i in xas:
    for j in ys:
        if i + j == 0:
            continue
        if j / (i+j) >= m and i+ j <= f and j / (i+j) <= e/(100+e):
            x = i
            y = j
            m = y / (x + y)
print(x+y, y)
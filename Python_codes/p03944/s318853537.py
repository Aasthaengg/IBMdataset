W, H, N = map(int, input().split())
xl, yl = 0, 0
xr, yr = W, H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        if x > xl:
            xl = x
    elif a == 2:
        if x < xr:
            xr = x
    elif a == 3:
        if y > yl:
            yl = y
    else:
        if y < yr:
            yr = y
    if xl >= xr or yl >= yr:
        print(0)
        exit()
print((xr - xl) * (yr - yl))
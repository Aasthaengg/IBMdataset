w, h, n = map(int, input().split())

xl, xr, yd, yu = 0, w, 0, h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        xl = max(xl, x)
    elif a == 2:
        xr = min(xr, x)
    elif a == 3:
        yd = max(yd, y)
    else:
        yu = min(yu, y)

width = max(xr-xl, 0)
height = max(yu-yd, 0)
print(width*height)

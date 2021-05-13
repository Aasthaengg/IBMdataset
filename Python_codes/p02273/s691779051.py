import math
n = int(input())

def three(p1x, p1y, p2x, p2y):
    dx = (p2x - p1x)
    dy = (p2y - p1y)
    sx = dx / 3 + p1x
    sy = dy / 3 + p1y
    tx = p2x - (dx / 3)
    ty = p2y - (dy / 3)

    mtx = tx - sx
    mty = ty - sy

    rad = math.radians(60)
    mux = mtx * math.cos(rad) - (mty * math.sin(rad))
    muy = mtx * math.sin(rad) + (mty * math.cos(rad))

    ux = mux + sx
    uy = muy + sy

    return [sx, sy, ux, uy, tx, ty]

def koch(p1x, p1y, p2x, p2y, n):
    if 0 == n:
        print('{:.8f} {:.8f}'.format(p1x, p1y))
    if 0 < n:
        sx, sy, ux, uy, tx, ty = three(p1x, p1y, p2x, p2y)
        koch(p1x, p1y, sx, sy, n - 1)
        koch(sx, sy, ux, uy, n - 1)
        koch(ux, uy, tx, ty, n - 1)
        koch(tx, ty, p2x, p2y, n - 1)

koch(0.00000000, 0.00000000, 100.00000000, 0.00000000, n)
print('{:.8f} {:.8f}'.format(100.00000000, 0.00000000))
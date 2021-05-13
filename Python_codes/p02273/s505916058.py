import math
cos = math.cos(math.radians(60))
sin = math.sin(math.radians(60))

def koch(count, p1x, p1y, p2x, p2y):
    global cos
    global sin
    if count == 0:
        return
    sx, sy = (2*p1x + p2x)/3, (2*p1y + p2y)/3
    tx, ty = (p1x + 2*p2x)/3, (p1y + 2*p2y)/3
    ux, uy = cos*(sx + tx) - sin*(ty - sy), sin*(tx - sx) + cos*(sy + ty)

    koch(count-1, p1x ,p1y, sx, sy)
    print(sx, sy)
    koch(count-1, sx, sy, ux, uy)
    print(ux, uy)
    koch(count-1, ux, uy, tx, ty)
    print(tx, ty)
    koch(count-1, tx, ty, p2x, p2y)

n = int(input())
print(0, 0)
koch(n, 0, 0, 100, 0)
print(100, 0)

import math

n = int(input())

def koch(c, px, py, qx, qy):
  if c > 0:
    sx = (2*px+qx)/3
    sy = (2*py+qy)/3
    tx = (px+2*qx)/3
    ty = (py+2*qy)/3
    ux = (tx-sx)*math.cos(math.radians(60))-(ty-sy)*math.sin(math.radians(60))+sx
    uy = (tx-sx)*math.sin(math.radians(60))+(ty-sy)*math.cos(math.radians(60))+sy
    koch(c-1, px, py, sx, sy)
    S = [sx, sy]
    print(" ".join(map(str, S)))
    koch(c-1, sx, sy, ux, uy)
    U = [ux, uy]
    print(" ".join(map(str, U)))    
    koch(c-1, ux, uy, tx, ty)
    T = [tx, ty]
    print(" ".join(map(str, T)))
    koch(c-1, tx, ty, qx, qy)

print("0 0")
koch(n, 0, 0, 100, 0)
print("100 0")

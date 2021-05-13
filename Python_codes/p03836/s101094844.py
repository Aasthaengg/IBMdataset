sx, sy ,tx, ty = map(int,input().split())
momo=""
xz = abs(tx-sx)
yz = abs(ty-sy)
momo += "U" * yz + "R" * xz + "D" * yz + "L" * xz
momo += "L" * 1 + "U" * (yz+1) + "R" * (xz+1) + "D" * 1
momo += "R" * 1 + "D" * (yz+1) + "L" * (xz+1) + "U" * 1
print(momo)
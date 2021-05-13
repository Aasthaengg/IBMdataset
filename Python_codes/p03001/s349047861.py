W, H, x, y = [int(n) for n in input().split()]

cx, cy = W/2, H/2

flg = 0
if x == cx and y == cy:
    flg = 1

print(W*H/2, flg)   
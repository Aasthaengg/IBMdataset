W, H, x, y = map(float, input().split())

center_x = W / 2
center_y = H / 2

area = W * H / 2

if center_x == x and center_y == y:
    print(f"{area} 1")
else:
    print(f"{area} 0")

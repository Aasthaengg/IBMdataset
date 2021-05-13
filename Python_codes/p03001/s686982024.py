W, H, x, y = map(int, input().split())

area = W*H/2
center_x = W/2
center_y = H/2

if center_x == x and center_y == y:
    print(area, 1)
else:
    print(area, 0)
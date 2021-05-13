w, h, x, y, r = map(int, input().split())

check_x = (x + r <= w) and (x - r >= 0)
check_y = (y + r <= h) and (y - r >= 0)

if check_x and check_y:
    print("Yes")
else:
    print("No")
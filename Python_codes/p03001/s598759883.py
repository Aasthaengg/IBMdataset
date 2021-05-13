W, H, x, y = map(int, input().split())

center = (W/2, H/2)

area = W*H

if (x, y) == center:
    print(area/2, 1)
else:
    print(area/2, 0)

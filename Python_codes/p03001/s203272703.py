w, h, x, y = map(int, input().split())
center_x = w / 2
center_y = h / 2
ans = w * h / 2
m = 1 if (center_x == x and center_y == y) else 0
print("{:.9f} {}".format(ans, m))

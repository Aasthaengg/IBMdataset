W, H, x, y = map(int, input().split())

max_area = float(W) * float(H) / 2.0
print("{} {}".format(max_area, 1 if 2*x == W and 2*y == H else 0))
c = input().split()
W, H, x, y, r = int(c[0]), int(c[1]), int(c[2]), int(c[3]), int(c[4])

if r <= x <= W - r and r <= y <= H - r:
    print("Yes")
else:
    print("No")


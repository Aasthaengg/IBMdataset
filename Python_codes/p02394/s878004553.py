W, H, x, y, r = [int(i) for i in input().split()]

if (x - r) < 0 or (x + r) > W:
    print("No")
elif (y - r) < 0 or (y + r) > H:
    print("No")
elif r > x:
    print("No")
elif r > y:
    print("No")
else:
    print("Yes")
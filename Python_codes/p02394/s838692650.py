w, h, x, y, r = [int(i) for i in input().split()]
if (x-r) >= 0 and (y+r) <= h and (x+r) <= w and (y-r) >= 0:
    print("Yes")
else:
    print("No")
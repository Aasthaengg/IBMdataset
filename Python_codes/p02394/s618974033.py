W, H, x, y, r = [int(i) for i in input().split()]
if x < 0 or y < 0:
    print("No")
elif x+r <= W and y+r <= H:
    print("Yes")
else:
    print("No")
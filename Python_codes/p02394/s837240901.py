W, H, x, y, r = [int(x) for x in input().split()]
if (0 <= x-r <= W) and (0 <= x+r <= W):
    if(0 <= y-r <= H) and (0 <= y+r <= H):
        print("Yes")
    else:
        print("No")
else:
    print("No")
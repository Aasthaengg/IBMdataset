a = input().split()
W,H = int(a[0]),int(a[1])
x,y = int(a[2]),int(a[3])
r = int(a[4])
if 0 <= (x-r) and (x+r) <= W:
    if 0 <= (y-r) and (y+r) <= H:
        print("Yes")
    else:
        print("No")
else:
    print("No")

W,H,x,y,r=map(int, input().split())
if W >= x+r and 0 <= x+r and H >= y+r and 0 <= y+r and x > 0 and y > 0:
    print("Yes")
else:
    print("No")
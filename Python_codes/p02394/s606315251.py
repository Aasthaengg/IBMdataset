W,H,x,y,r = [int(i) for i in input().split()]
w1 = r
h1 = r
w2 = W-r
h2 = H-r
if w1 <= x <= w2 and h1 <= y <= h2:
    print("Yes")
else:
    print("No")

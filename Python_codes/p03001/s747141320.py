W,H,x,y = list(map(int,input().split()))
out = W*H/2
if W %2 == 0 and H %2 == 0 and x == W//2 and y == H//2:
    print(str(out)+' '+str(1))
else:
    print(str(out)+' '+str(0))
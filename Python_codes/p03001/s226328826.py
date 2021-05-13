W,H,X,Y = map(int,input().split())
if W == X*2 and H == Y*2:
    f = 1
else:
    f = 0
print(W*H/2, f)

H,W = map(int, input().split())
if H == W == 1:
    print(1)
    exit()
if H == 1 or W == 1:
    print (max(W,H)-2)
    exit()
print(W*H - (2*H+2*W-4))
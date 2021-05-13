W,H,x,y = map(int,input().split())
if x == 0.5*W and y == 0.5*H:
    b = 1
else:
    b = 0
print(0.5*W*H, b)
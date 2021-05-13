W,H,x,y = map(int,input().split())
is_center = 0
if x == W/2 and y == H/2:
    is_center = 1
print((W*H)/2,is_center)

W, H, x, y = map(int,input().split())

cx = W/2
cy = H/2

area = (W*H)/2
if x==cx and y==cy:
    judge = 1
else:
    judge = 0

print(f'{area:.09f}', judge)
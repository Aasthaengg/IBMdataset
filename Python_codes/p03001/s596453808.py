W, H, x, y=map(int,input().split())

mx=W*H/2
mul=0
if x==W/2 and y==H/2:
    mul=1

print(mx, mul)
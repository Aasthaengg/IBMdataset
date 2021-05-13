w,h,x,y = map(int,input().split())

half = w*h/2
msg = 0
if x == w/2 and y == h/2:
    msg = 1
print(half, msg)
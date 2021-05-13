w,h,x,y = map(int,input().split())
xx = w-x
yy = h-y
if x == xx and y == yy:
    a = 1
else:
    a = 0
print(w*h/2,a)
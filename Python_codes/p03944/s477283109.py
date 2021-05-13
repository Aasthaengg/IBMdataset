w,h,n = map(int,input().split())

min_w = 0
max_w = w
min_h = 0
max_h = h

for i in range(n):
    x,y,a = map(int,input().split())
    if a == 1:
        min_w = max(x,min_w)
    elif a == 2:
        max_w = min(x,max_w)
    elif a == 3:
        min_h = max(y,min_h)
    elif a == 4:
        max_h = min(y,max_h)

if (max_h - min_h) <= 0 or (max_w - min_w) <= 0:
    print(0)
else:
    print((max_h - min_h)*(max_w - min_w))

    

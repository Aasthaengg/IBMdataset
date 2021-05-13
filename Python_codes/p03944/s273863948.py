w,h,n = map(int,input().split())
x_a = 0
y_a = 0
for i in range(n):
    x,y,a = map(int,input().split())
    
    if a == 1:
        if x < x_a:
            x_a = x_a
        else:
            x_a = x
    elif a == 2:
        if x < w:
            w = x
        else:
            w = w
        
    elif a == 3:
        if y < y_a:
            y_a = y_a
        else:
            y_a = y
    
    elif a == 4:
        if y < h:
            h = y
        else:
            h = h

if w - x_a <= 0 or h - y_a <= 0:
    ans = 0
else:
    ans = (w - x_a)*(h - y_a)

print(ans)
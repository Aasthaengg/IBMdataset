w,h,n = map(int,input().split())
#x_list = [int(1) for i in range(w+1)]
#y_list = [int(1) for i in range(h+1)]
#print(x_list)
#print(y_list)
min_x = 0
max_x = w
min_y = 0
max_y = h
for i in range(n):
    x,y,a = map(int,input().split())
    if a==1:
        min_x = max(min_x,x)
    elif a==2:
        max_x = min(max_x,x)
    elif a==3:
        min_y = max(min_y,y)
    else:
        max_y = min(max_y,y)
if min_x > max_x or min_y > max_y:
    print(0)
else:
    print((max_x-min_x)*(max_y-min_y))
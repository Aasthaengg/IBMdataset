n,m,x,y = map(int,input().split())
x_max = max(list(map(int,input().split())))
y_min = min(list(map(int,input().split())))
if x_max+1<=y_min:
    if x_max+1>x and x_max+1<=y:
        print('No War')
    else:
        print('War')
else:
    print('War')
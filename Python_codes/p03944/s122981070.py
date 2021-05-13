whn_list = list(map(int,input().split()))
x_y_list = []
x = [0,whn_list[0]]
y = [0,whn_list[1]]

for i in range(whn_list[2]):
    x_y_list.append(list(map(int,input().split())))

for i in x_y_list:
    if i[2] == 1:
        x[0] = max(i[0],x[0])
    elif i[2] == 2:
        x[1] = min(i[0],x[1])
    elif i[2] == 3:
        y[0] = max(i[1],y[0])
    else:
        y[1] = min(i[1],y[1])

s = (x[1]-x[0])*(y[1]-y[0])

if  (x[1] <= x[0]) or (y[1] <= y[0]):
    print(0)
else:
    print(s)
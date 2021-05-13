W, H, N = map(int,input().split())

lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))


x_left,x_right = 0, W
y_under, y_up = 0,H

for i in range(N):
    x,y = lst[i][0], lst[i][1]
    if lst[i][2] == 1:
        if x_left < x: 
            x_left = x
    elif lst[i][2] == 2:
        if x_right > x:
            x_right = x
            if x_right == 0:
                print(0)
                exit()
    elif lst[i][2] == 3:
        if y_under < y:
            y_under = y
    elif lst[i][2] == 4:
        if y_up > y:
            y_up = y
            if y_up == 0:
                print(0)
                exit()

yoko = x_right - x_left
tate = y_up - y_under
if tate * yoko <= 0:
    print(0)
else:
    print(tate * yoko)

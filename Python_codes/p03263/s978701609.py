def make_path(l,y1,x1,y2,x2):
    current_x = x1
    current_y = y1
    if x2 == x1:
        for i in range(y2-y1):
            l.append((current_y,current_x,current_y+1,current_x))
            current_y += 1
    elif x2 > x1:
        if y1 % 2 == 1:
            for i in range(x2-x1):
                l.append((current_y,current_x,current_y,current_x+1))
                current_x += 1
            for i in range(y2-y1):
                l.append((current_y,current_x,current_y+1,current_x))
                current_y += 1
        else:
            l.append((current_y,current_x,current_y+1,current_x))
            current_y += 1
            for i in range(x2-x1):
                l.append((current_y,current_x,current_y,current_x+1))
                current_x += 1
            for i in range(y2-y1-1):
                l.append((current_y,current_x,current_y+1,current_x))
                current_y += 1
    else:
        if y1 % 2 == 1:
            l.append((current_y,current_x,current_y+1,current_x))
            current_y += 1
            for i in range(x1-x2):
                l.append((current_y,current_x,current_y,current_x-1))
                current_x -= 1
            for i in range(y2-y1-1):
                l.append((current_y,current_x,current_y+1,current_x))
                current_y += 1
        else:
            for i in range(x1-x2):
                l.append((current_y,current_x,current_y,current_x-1))
                current_x -= 1
            for i in range(y2-y1):
                l.append((current_y,current_x,current_y+1,current_x))
                current_y += 1
                
import numpy as np

H,W,*af = map(int, open(0).read().split())
a = np.array(af).reshape(H,W).tolist()
ab = [[x % 2 for x in y] for y in a]
rev = False
found_first = False
ans = []
temp = [0] * 4
x_count = 0
y_count = 0
for y in ab:
    y_count += 1
    if rev == False:
        x_count += 1
        for x in y:
            if x == 1:
                if found_first == False:
                    temp[0] = y_count
                    temp[1] = x_count
                    found_first = True
                else:
                    temp[2] = y_count
                    temp[3] = x_count
                    make_path(ans,*temp)
                    found_first = False
            x_count += 1
        rev = True
    else:
        x_count -= 1
        for x in reversed(y):
            if x == 1:
                if found_first == False:
                    temp[0] = y_count
                    temp[1] = x_count
                    found_first = True
                else:
                    temp[2] = y_count
                    temp[3] = x_count
                    make_path(ans,*temp)
                    found_first = False
            x_count -= 1
        rev = False
print(len(ans))
for x in ans:
    print(*x)
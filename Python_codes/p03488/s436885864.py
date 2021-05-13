s = input()
x,y = map(int,input().split())
cur_x = 0
cur_y = 0
L_x = []
L_y = []
s += 'K'
temp = 0
dirc = 'yoko'
for i in range(len(s)):
    if s[i] == 'F':
        temp += 1
    elif s[i] == 'T':
        if temp == 0:
            if dirc == 'yoko':
                dirc = 'tate'
            else:
                dirc = 'yoko'
        else:
            if dirc == 'yoko':
                L_x.append(temp)
                temp = 0
                dirc = 'tate'
            else:
                L_y.append(temp)
                temp = 0
                dirc = 'yoko'
    else:
        if temp != 0:
            if dirc == 'yoko':
                L_x.append(temp)
                temp = 0
                dirc = 'tate'
            else:
                L_y.append(temp)
                temp = 0
                dirc = 'yoko'
dp_x = [[False]*8001 for i in range(len(L_x)+1)]
dp_y = [[False]*8001 for i in range(len(L_y)+1)]
dp_x[0][0] = True
dp_y[0][0] = True
if s[0] != 'F':
    for i in range(1,len(L_x)+1):
        for j in range(8001):
            if j+L_x[i-1] <= 8000:
                dp_x[i][j] = dp_x[i-1][abs(j-L_x[i-1])] or dp_x[i-1][j+L_x[i-1]]
            else:
                dp_x[i][j] = dp_x[i-1][abs(j-L_x[i-1])]
    for i in range(1,len(L_y)+1):
        for j in range(8001):
            if j+L_y[i-1] <= 8000:
                dp_y[i][j] = dp_y[i-1][abs(j-L_y[i-1])] or dp_y[i-1][j+L_y[i-1]]
            else:
                dp_y[i][j] = dp_y[i-1][abs(j-L_y[i-1])]
    if dp_x[len(L_x)][abs(x)] == True and dp_y[len(L_y)][abs(y)] == True:
        print('Yes')
    else:
        print('No')
else:
    for i in range(2,len(L_x)+1):
        for j in range(8001):
            if j+L_x[i-1] <= 8000 and abs(j-L_x[i-1]) <= 8000:
                dp_x[i-1][j] = dp_x[i-2][abs(j-L_x[i-1])] or dp_x[i-2][j+L_x[i-1]]
            elif abs(j-L_x[i-1]) <= 8000:
                dp_x[i-1][j] = dp_x[i-2][abs(j-L_x[i-1])]
    for i in range(1,len(L_y)+1):
        for j in range(8001):
            if j+L_y[i-1] <= 8000 and abs(j-L_y[i-1]) <= 8000:
                dp_y[i][j] = dp_y[i-1][abs(j-L_y[i-1])] or dp_y[i-1][j+L_y[i-1]]
            elif abs(j-L_y[i-1]) <= 8000:
                dp_y[i][j] = dp_y[i-1][abs(j-L_y[i-1])]
    if abs(x-L_x[0]) <= 8000:
        if dp_x[len(L_x)-1][abs(x-L_x[0])] == True and dp_y[len(L_y)][abs(y)] == True:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
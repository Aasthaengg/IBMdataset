

import math





H,W = list(map(int,input().split(" ")))
x1 = 0
y1 = 0
x2 = 0
y2 = 0
cond = 0
mass = []
for _ in range(H):
    mass.append(list(map(int, input().split(" "))))

s = [0]
def move(sx,sy,gx,gy):
    temp = []
    go = -1
    if sy % 2 == 1:
        go = 1 #
    x = sx
    y = sy
    while True:

        # 現在地の確認

        if (x == W and go == 1) or (x == 1 and go == -1): #端っこにいるなら下がる→反転
            ny = y + 1
            temp.append([y, x, ny, x])
            s[0] += 1
            y = ny #下がる
            go *= -1
            if x == gx and y == gy:
                return temp



        nx = x + go
        temp.append([y, x, y, nx])
        s[0] += 1
        x = nx

        # check
        if  x == gx and  y ==gy:
            return temp






ans = []
for y,As in enumerate(mass):
    if y %2 == 0:
        start = 0
        end = W
        hoge = 1
    else:
        start = W-1
        end = -1
        hoge = -1
    for i in range(start,end,hoge):
        a = As[i]
        if a % 2 == 1:
            if cond %2 == 0:
                x1 = i + 1
                y1 = y + 1
                cond += 1
            else:
                x2 = i + 1
                y2 = y + 1
                ans.append(move(x1,y1,x2,y2))
                # if x2 > x1:
                #     step = -1
                # else:
                #     step = 1
                # cot  = abs(x2 -x1)
                # for _ in range(cot): #横に動く
                #     ans.append([y2,x2,y2,x2+step])
                #     x2 = x2+step
                # cot = abs(y2 -y1)
                # for _ in range(cot):
                #     ans.append([y2,x2,  y2 -1, x2])
                #     y2 = y2 -1
                cond += 1

print(s[0])
for temp in ans:
    for temp2 in temp:
        print(*temp2 )
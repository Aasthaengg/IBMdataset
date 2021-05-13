s = input()
x, y = map(int, input().split())
n = len(s)
#dp_x: +, -に向いてて行けるかどうか
dp_x = [[False, False] for i in range(2*n+2)]
dp_y = [[False, False] for i in range(2*n+2)]
dp_x[0][0] = True
dp_y[0][0] = True
dp_y[0][1] = True

flag = 0
for i in range(len(s)):
    if s[i] == "T":
        if flag == 0:
            flag = 2
            for j in range(-i-1, i+2):
                if dp_x[j][0]:
                    dp_x[j][1] = True

        elif flag == 2:
            flag = 1
            for j in range(-i-1, i+2):
                dp_x[j][0] = dp_x[j][1] or dp_x[j][0]
                dp_x[j][1] = dp_x[j][1] or dp_x[j][0]

        else:
            flag = 2
            for j in range(-i-1, i+2):
                dp_y[j][0] = dp_y[j][1] or dp_y[j][0]
                dp_y[j][1] = dp_y[j][1] or dp_y[j][0]


    else:
        if flag == 0:
            for j in range(i+1, -i-2, -1):
                dp_x[j][0] = dp_x[j-1][0]

        elif flag == 1:
            for j in range(i+1, -i-2, -1):
                dp_x[j][0] = dp_x[j-1][0]
                dp_x[-j][1] = dp_x[-j+1][1]
        else:
            for j in range(i+1, -i-2, -1):
                dp_y[j][0] = dp_y[j-1][0]
                dp_y[-j][1] = dp_y[-j+1][1]


if dp_x[x][0] or dp_x[x][1]:
    if dp_y[y][0] or dp_y[y][1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")

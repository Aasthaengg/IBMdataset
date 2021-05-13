n = int(input())
array = [input().split() for i in range(n)]
b_1 = []
b_2 = []
b_3 = []
b_4 = []
zero = "0 0 0 0 0 0 0 0 0 0"
for i in range(3):
    b_1.append(zero.split())
    b_2.append(zero.split())
    b_3.append(zero.split())
    b_4.append(zero.split())
for i in range(n):
    b = int(array[i][0])
    f = int(array[i][1])
    r = int(array[i][2])
    v = int(array[i][3])
    if b == 1:
        b_1[f-1][r-1] = str(int(b_1[f-1][r-1])+v)
    elif b == 2:
        b_2[f-1][r-1] = str(int(b_2[f-1][r-1])+v)
    elif b == 3:
        b_3[f-1][r-1] = str(int(b_3[f-1][r-1])+v)
    else:
        b_4[f-1][r-1] = str(int(b_4[f-1][r-1])+v)
for i in range(4):
    for i2 in range(3):
        for i3 in range(10):
            if i == 0:
                if i3 == 9:
                    print(b_1[i2][i3])
                elif i3 == 0:
                    print(" "+b_1[i2][i3],end=" ")
                else:
                    print(b_1[i2][i3],end=" ")
            elif i == 1:
                if i3 == 9:
                    print(b_2[i2][i3])
                elif i3 == 0:
                    print(" "+b_2[i2][i3],end=" ")
                else:
                    print(b_2[i2][i3],end=" ")
            elif i == 2:
                if i3 == 9:
                    print(b_3[i2][i3])
                elif i3 == 0:
                    print(" "+b_3[i2][i3],end=" ")
                else:
                    print(b_3[i2][i3],end=" ")
            else:
                if i3 == 9:
                    print(b_4[i2][i3])
                elif i3 == 0:
                    print(" "+b_4[i2][i3],end=" ")
                else:
                    print(b_4[i2][i3],end=" ")
    if i == 3:
        break
    else:
        print("####################")
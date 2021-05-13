a = [list(map(int,input().split())) for i in range(3)]
n = int(input())
for k in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = -1
f = False
for i in range(3):
    for j in range(3):
        if (a[0][0] == a[0][1] == a[0][2]== -1) or (a[1][0] == a[1][1] == a[1][2]== -1) or (a[2][0] == a[2][1] == a[2][2]== -1):
            f = True
        elif (a[0][0] == a[1][0] == a[2][0] == -1) or (a[0][1] == a[1][1] == a[2][1] == -1) or (a[0][2] == a[1][2] == a[2][2] == -1):
            f = True
        elif (a[0][0] == a[1][1] == a[2][2] == -1) or (a[2][0] == a[1][1] == a[0][2] == -1):
            f = True
if f:
    print('Yes')
else:
    print('No')
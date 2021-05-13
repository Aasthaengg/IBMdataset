c = [list(map(int, input().split())) for _ in range(3)]
a = [None, None, None]
b = [None, None, None]
a[0] = 0

b[0] = c[0][0] - a[0]
b[1] = c[0][1] - a[0]
b[2] = c[0][2] - a[0]

a[1] = c[1][0] - b[0]
a[2] = c[2][0] - b[0]
for i in range(3):
    for j in range(3):
        if c[i][j] != a[i]+b[j]:
            print("No")
            exit()
print("Yes")
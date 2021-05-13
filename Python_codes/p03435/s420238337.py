C=list(list(map(int,input().split())) for i in range(3))
for a in range(3):
    if (C[a][0]-C[a][1]!=C[0][0]-C[0][1] or C[a][1]-C[a][2]!=C[0][1]-C[0][2]):
        print("No")
        exit()
for b in range(3):
    if (C[0][b]-C[1][b]!=C[0][0]-C[1][0] or C[1][b]-C[2][b]!=C[1][0]-C[2][0]):
        print("No")
        exit()
print("Yes")

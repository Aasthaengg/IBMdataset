c = [list(map(int,input().split())) for _ in range(3)]
for i in range(3):
    for j in range(i+1,3):
        t = c[i][0]-c[j][0]
        for k in [1,2]:
            if t != c[i][k]-c[j][k]:
                print("No")
                exit(0)
        t = c[0][i]-c[0][j]
        for k in [1,2]:
            if t != c[k][i]-c[k][j]:
                print("No")
                exit(0)
print("Yes")
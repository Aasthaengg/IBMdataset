C=[list(map(int,input().split())) for i in range(3)]
a1=0
b=C[0]
a=[C[i][0]-b[0] for i in range(3)]
for i in range(3):
    for j in range(3):
        if C[i][j]!=a[i]+b[j]:
            print("No")
            exit()
print("Yes")
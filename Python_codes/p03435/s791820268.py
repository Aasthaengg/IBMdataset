c=[list(map(int,list(input().split()))) for _ in range(3)]
a=[0]*3
b=[0]*3

for i in range(3):
    b[i]=c[0][i]-a[0]
a[1]=c[1][0]-b[0]
a[2]=c[2][0]-b[0]

ans="Yes"
for i in range(3):
    for j in range(3):
        if c[i][j]!=a[i]+b[j]:
            ans="No"
            break
print(ans)
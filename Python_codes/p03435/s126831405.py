c=[list(map(int,input().split())) for i in range(3)]

bl=c[0]
a2=c[1][0]-bl[0]
a3=c[2][0]-bl[0]
al=[0,a2,a3]
flag='Yes'
for i in range(3):
    for j in range(3):
        if c[i][j]!=al[i]+bl[j]:
            flag='No'
            break
print(flag)



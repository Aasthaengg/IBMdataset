n,c=map(int,input().split())
irohen=[list(map(int,input().split())) for i in range(c)]
grid=[list(map(int,input().split())) for i in range(n)]
rem0=[0]*c
rem1=[0]*c
rem2=[0]*c
for i in range(n):
    for j in range(n):
        if (i+j)%3==0:
            rem0[grid[i][j]-1]+=1
        elif (i+j)%3==1:
            rem1[grid[i][j]-1]+=1
        elif (i+j)%3==2:
            rem2[grid[i][j]-1]+=1
ans=10**10
for i in range(c):
    for j in range(c):
        for h in range(c):
            chk=0
            if i==j or i==h or j==h:
                continue
            for k in range(c):
                chk+=rem0[k]*irohen[k][i]+rem1[k]*irohen[k][j]+rem2[k]*irohen[k][h]
            if chk < ans:ans=chk
print(ans)

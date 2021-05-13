c=[[0 for i in range(9)] for i in range(9)]

n=int(input())
for i in range(1,n+1):
    I=str(i)
    if I[0]!="0" and I[len(I)-1]!="0":
        c[int(I[0])-1][int(I[len(I)-1])-1]+=1

s=0
for i in range(9):
    for j in range(9):
        s+=c[i][j]*c[j][i]

print(s)
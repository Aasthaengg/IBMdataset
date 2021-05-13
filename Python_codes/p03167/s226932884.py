h,w=map(int,input().split())
mat=[]
for i in range(h):
    a=[i for i in list(input())]
    mat.append(a)
for i in range(w):
    if mat[0][i]=='.':
        mat[0][i]=1
    else:
        for j in range(i,w):
            mat[0][j]=0
        break
for i in range(1,h):
    for j in range(w):
        if mat[i][j]=='.':
            mat[i][j]=0
            mat[i][j]=(mat[i][j]+mat[i-1][j])%1000000007
            if j-1>=0:
                mat[i][j]=(mat[i][j]+mat[i][j-1])%1000000007
        else:
            mat[i][j]=0

print(mat[h-1][w-1])

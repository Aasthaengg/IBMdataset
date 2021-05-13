r,c=map(int,input().split())
tbl=[[0]*c for i in range(r+1)]
for i in range(r):
    tbl[i]=list(map(int,input().split()))
for i in range(c):
    for j in range(r):
        tbl[r][i] +=tbl[j][i]
for i in range(r+1):
    m=0
    for j in range(c):
        m += tbl[i][j]
        print(tbl[i][j],end=" ")
    print(m)

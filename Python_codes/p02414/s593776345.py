n,m,l=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
b=[list(map(int,input().split())) for j in range(m)]
c=[[0]*l for r in range(n)]
for i in range(n):
    for j in range(l):
        for r in range(m):
            c[i][j]+=a[i][r]*b[r][j]
    print(' '.join(map(str,c[i])))

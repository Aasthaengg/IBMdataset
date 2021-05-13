n,m,l=map(int,input().split())
a=[]
for i in range (n):
    a.append(list(map(int,input().split())))
b=[]
for i in range (m):
    b.append(list(map(int,input().split())))
for i in range(n):
    for j in range(l):
        c=0
        for k in range(m):
            c+=a[i][k]*b[k][j]
        if j == l-1:
            print(c)
        else:
            print(c,end=" ")

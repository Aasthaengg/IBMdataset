n,m,l=map(int,input().split())
a=list()
b=list()
for i in range(n):
    x=list(map(int,input().split()))
    a.append(x)
for i in range(m):
    y=list(map(int,input().split()))
    b.append(y)
for i in range(n):
    line=list()
    for j in range(l):
        sum=0
        for k in range(m):
            sum+=a[i][k]*b[k][j]
        line.append(sum)
    print(" ".join(list(map(str,line))))


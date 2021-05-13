n,m,l=[int(i) for i in input().split()]
x=[[int(0) for i in range(m)]for j in range(n)]
z=[[int(0) for i in range(l)]for j in range(n)]
y=[[int(0)for i in range(l)]for j in range(m)]
for i in range(n):
    k=input().split()
    for j in range(m):
        x[i][j]=int(k[j])
for i in  range(m):
    k=input().split()
    for j in range(l):
        y[i][j]=int(k[j])
        
for i in range(n):
    for j in range(l):
        count=int(0)
        for v in range(m):
            count=count+x[i][v]*y[v][j]
        z[i][j]=count
        
for i in range(n):
    for j in range(l-1):
        print(z[i][j],"",end="")
    print(z[i][l-1])
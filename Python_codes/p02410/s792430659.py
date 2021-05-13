n,m=map(int,input().split())
a=[]
b=[]
z=[]
x=[]
for i in range(n):
    a+=[[int(i) for i in input().split()]]
for i in range(m):
    b+=[[int(i) for i in input().split()]]
for i in range(n):
    for j in range(m):
        z+=[a[i][j]*b[j][0]]
    x+=[sum(z)]
    z=[]
for i in range(n):
    print(x[i])
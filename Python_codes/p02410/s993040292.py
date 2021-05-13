x=[]
y=[]
n,m=map(int,input().split())
for i in range(n):
    x.append([])
for i in range(n):
    y=list(map(int,input().split()))
    x[i].extend(y)

b=[]
for i in range(m):
    j=int(input())
    b.append(j)

for i in range(n):
    sum=0
    for j in range(m):
        sum+=x[i][j]*b[j]
    print(sum)
n,m= list(map(int, input().strip().split()))
a = []
for i in range(m):
    a.append(list(map(int, input().strip().split())))
b=[0]*(2*m)
for i in range(m):
    b[2*i]=a[i][0]
    b[2*i+1]=a[i][1]
for i in range(n):
    print(b.count(i+1))
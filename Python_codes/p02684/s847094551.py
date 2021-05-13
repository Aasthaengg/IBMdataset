n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    a[i]-=1
doubling=[[0 for i in range(n)] for j in range(60)]
for i in range(n):
    doubling[0][i]=a[i]
for i in range(59):
    for j in range(n):
        doubling[i+1][j]=doubling[i][doubling[i][j]]
v=0
for d in range(60):
    if(k>>d &1):
        v=doubling[d][v]

print(v+1)
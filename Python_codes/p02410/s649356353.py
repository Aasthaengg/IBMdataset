n,m=map(int,input().split())
ms=[[] for _ in range(n)]
for i in range(n):
    ms[i]=list(map(int,input().split()))
x=[0 for _ in range(m)]
for j in range(m):
    x[j]=int(input())
y=[0 for _ in range(n)]
for i in range(n):
    for j in range(m):
        y[i] += ms[i][j] * x[j]
    print(y[i])
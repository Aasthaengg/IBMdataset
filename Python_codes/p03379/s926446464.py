n = int(input())
x = list(map(int,input().split()))
y = sorted(x)
m1,m2 = y[n//2-1],y[n//2]
for i in x:
    if i<=m1: print(m2)
    else: print(m1)
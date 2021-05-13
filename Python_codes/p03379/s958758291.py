n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
m=n//2
z=y[m-1]
for i in range(n):
    if x[i]<=y[m-1]:
        print(y[m])
    else:
        print(y[m-1])


n=int(input())
a=[0]+[int(x) for x in input().split()]
x=[0]*(n+1)

for i in range(1,n+1):
    x[1]+=(-1)**(i+1)*a[i]

for i in range(2,n+1):
    x[i]=2*a[i-1]-x[i-1]

x.pop(0)

print(*x)
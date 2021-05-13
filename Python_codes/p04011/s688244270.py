n=int(input())
k=int(input())
x=int(input())
y=int(input())

sale=0

if n<=k:
    sale+=n*x
else:
    sale+=k*x+y*(n-k)

print(sale)

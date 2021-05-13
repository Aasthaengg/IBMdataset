n,m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

xlen=0
ylen=0

for i in range(1,n):
    xlen+=i*(n-i)*(x[i]-x[i-1])

for i in range(1,m):
    ylen+=i*(m-i)*(y[i]-y[i-1])

print(xlen*ylen%(10**9+7))
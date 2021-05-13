mod=10**9+7
n, m=map(int,input().split())
x=tuple(map(int,input().split()))
y=tuple(map(int,input().split()))

lx, ly=0, 0
for i in range(n):
    lx+= i*x[i]-(n-i-1)*x[i]
    lx%=mod
for i in range(m):
    ly+= i*y[i]-(m-i-1)*y[i]
    ly%=mod

print((lx*ly)%mod)
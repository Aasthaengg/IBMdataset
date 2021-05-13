mod = 10**9+7
n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.sort()
y.sort()

xd = 0
for i in range(n):
    xd += (2*i-n+1)*x[i]
    xd %= mod

yd = 0
for i in range(m):
    yd += (2*i-m+1)*y[i]
    yd %= mod

print(xd*yd%mod)
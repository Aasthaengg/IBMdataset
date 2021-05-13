n,m=[int(j) for j in input().split()]
x=[int(j) for j in input().split()]
y=[int(j) for j in input().split()]
mod=10**9+7
sx=0
sy=0
for i in range(n):
    sx+=(2*i-n+1)*x[i]
    sx=sx%mod
for i in range(m):
    sy+=(2*i-m+1)*y[i]
    sy=sy%mod

print((sx*sy)%mod)




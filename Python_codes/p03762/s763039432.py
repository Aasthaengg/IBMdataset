n,m = map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
mod = 10**9+7

lx = [x[i+1]-x[i] for i in range(n-1)]
ly = [y[i+1]-y[i] for i in range(m-1)]
lsum = [0]
for i in range(10**5+5):
    lsum.append((lsum[i]+i+1)%mod)

xres = 0
for i in range(1,n):
    xsum = 0
    kaisuu = min(i,n-i)
    xsum += lsum[kaisuu-1]*2
    xsum += kaisuu * (n-1-2*(kaisuu-1))
    xsum %= mod
    xsum = (xsum * lx[i-1])%mod
    xres += xsum
xres %= mod

yres = 0
for i in range(1,m):
    ysum = 0
    kaisuu = min(i,m-i)
    ysum += lsum[kaisuu-1]*2
    ysum += kaisuu * (m-1-2*(kaisuu-1))
    ysum %= mod
    ysum = (ysum * ly[i-1])%mod
    yres += ysum
yres %= mod

print((xres*yres)%mod)


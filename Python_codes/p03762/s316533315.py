from itertools import accumulate
n,m=map(int,input().split())
*x,=map(int,input().split())
*y,=map(int,input().split())

mod=10**9+7

xsum=list(accumulate(x))
ysum=list(accumulate(y))
xt=0
yt=0
for i in range(1,n):
    xt+=i*x[i]-xsum[i-1]
    xt%=mod

for i in range(1,m):
    yt+=i*y[i]-ysum[i-1]
    yt%=mod

print(xt*yt%mod)

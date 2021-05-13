n,m=[int(x) for x in input().split()]
x=[int(x) for x in input().split()]
y=[int(x) for x in input().split()]
mod=10**9+7
ans=0
ysum=0
for j in range(1,m):
    ysum+=(y[j]-y[j-1])*j*(m-j)
for i in range(1,n):
    ans=ans+(x[i]-x[i-1])*i*(n-i)*ysum
print(ans%mod)
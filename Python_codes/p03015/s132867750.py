l=list(input())
n=len(l)
mod=10**9+7
dp1=[0]*(n+1)
dp2=[0]*(n+1)
dp2[0]=1
for i in range(n):
  if l[i]=='1':
    dp2[i+1]=dp2[i]*2%mod
    dp1[i+1]=(dp2[i]+dp1[i]*3)%mod
  else:
    dp2[i+1]=dp2[i]%mod
    dp1[i+1]=dp1[i]*3%mod
print((dp1[-1]+dp2[-1])%mod)
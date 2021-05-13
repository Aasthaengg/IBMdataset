l=input()
mod=10**9+7
n=len(l)
dp1=[1]
dp2=[1]
for i in range(1,n+1):
  dp1.append((dp1[i-1]*3)%mod)
  dp2.append(dp2[i-1])
  if l[n-i]=='1':
    dp2[i]=(dp2[i]*2+dp1[i-1])%mod
print(dp2[n])
l=input()
mod=10**9+7
dp0=[0]*(len(l)+1)
dp1=[0]*(len(l)+1)
dp0[0]=1
for i in range(len(l)):
	if l[i]=="1":
		dp0[i+1]=dp0[i]*2%mod
		dp1[i+1]=(dp0[i]+dp1[i]*3)%mod
	else:
		dp0[i+1]=dp0[i]
		dp1[i+1]=dp1[i]*3%mod
print((dp0[-1]+dp1[-1])%mod)
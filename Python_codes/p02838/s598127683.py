n=int(input())
A=list(map(int,input().split()))
MOD=10**9+7
O=[0]*61
Z=[0]*61
for a in A:
	for i in range(61):
		if (1<<i)&a:
			O[i]+=1
		else:
			Z[i]+=1
	
R=0
for i in range(61):
	R+=pow(2,i,MOD)*O[i]%MOD*Z[i]%MOD
	R%=MOD

print(R)
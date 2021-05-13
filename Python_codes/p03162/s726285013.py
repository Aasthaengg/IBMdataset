n=int(input()) 
dp1,dp2,dp3=[0]*n,[0]*n,[0]*n
f=[]
for i in range(n):
	f.append([int(x) for x in input().split()])  
dp1[0]=f[0][0] 
dp2[0]=f[0][1] 
dp3[0]=f[0][2] 
for i in range(1,n):
	dp1[i]=f[i][0]+max(dp2[i-1],dp3[i-1]) 
	dp2[i]=f[i][1]+max(dp1[i-1],dp3[i-1])
	dp3[i]=f[i][2]+max(dp2[i-1],dp1[i-1])
print(max(dp1[-1],dp2[-1],dp3[-1])) 
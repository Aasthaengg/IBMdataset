n = int(input())
t = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
x,flag,ans,mod = [[t[0],t[0]]]+[[1,1] for _ in range(n-1)],True,1,10**9+7
if max(t)!=max(a): flag = False
for i in range(1,n):
	if t[i-1]<t[i]: x[i] = [t[i],t[i]]
	else: x[i][0] = t[i]
if x[-1][0]<a[-1]: flag = False
else:
	x[-1] = [a[-1],a[-1]]
	for i in range(n-2,0,-1):
		if a[i]>a[i+1]:
			if x[i][0]>=a[i]: x[i]=[a[i],a[i]]
			else: flag = False
		else:
			if x[i][0]>=a[i]: x[i][0]=a[i]
			else: pass
if flag:
	for i,j in x: ans = (ans*(i-j+1))%mod
else: ans = 0
print(ans)
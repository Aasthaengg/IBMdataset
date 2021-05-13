n=int(input())
a=[]
for _ in range(n):
	a.append(list(map(int,input().split())))
from copy import deepcopy
b=deepcopy(a)
for i in range(n):
	for j in range(n):
		for k in range(n):
			b[j][k]=min(b[j][i]+b[i][k],b[j][k])
if a!=b:
	print(-1)
	exit()
ans=0
for i in range(n):
	b[i][i]=10**18
for i in range(n):
	for j in range(n):
		f=1
		for k in range(n):
			if b[i][j]>=b[i][k]+b[k][j]:
				f=0
				break
		if f:
			ans+=b[i][j]
print(ans//2)

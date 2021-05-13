n=int(input())
a=[0]+list(map(int,input().split()))
b=list(map(int,input().split()))+[0]

m=[a[i] for i in range(1,n+1)]
l=[1 for _ in range(n)]

for i in range(n):
	if a[i]<a[i+1]:
		l[i]=a[i+1]
		
ans=1
for i in range(n-1,-1,-1):
	if b[i+1]<b[i]:
		if l[i]>b[i]:
			ans=0
		else:
			l[i]=b[i]
	m[i]=min(m[i],b[i])
	
for i in range(n):
	ans=(ans*(m[i]-l[i]+1))%(10**9+7)
	if m[i]<l[i]:
		ans=0
print(ans)
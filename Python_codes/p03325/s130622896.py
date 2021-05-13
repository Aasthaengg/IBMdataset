n=int(input())
a=list(map(int,input().split()))
cnt=0
f=True
while f:
	for i in range(n):
		if a[i]>2 and a[i]%2==0:
			a[i]=a[i]//2
			cnt+=1
		else:
			a[i]=3*a[i]
			
	for ai in a:
		if ai%2==0:
			break
	else:
		f=False
			
print(cnt)
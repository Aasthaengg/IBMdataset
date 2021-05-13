x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
ans=[]
for i in range(min(x,k+1)):
	for j in range(y):
		if (i+1)*(j+1)>k:
			break
		for l in range(z):
			if (i+1)*(j+1)*(l+1)<=k:
				ans.append(a[i]+b[j]+c[l])
			else:
				break
ans.sort()
for i in range(k):
	print(ans[-i-1])
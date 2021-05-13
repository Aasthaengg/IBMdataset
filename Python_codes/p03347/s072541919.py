n=int(input())
a=[int(input())for _ in range(n)]
a=a[::-1]
cnt=0
ans=0
for i in range(n):
	if cnt==0:
		if a[i]!=0:
			cnt=a[i]
			ans+=a[i]
	else:
		cnt-=1
		if a[i]>cnt:
			cnt=a[i]
			ans+=a[i]
		elif a[i]<cnt:
			print(-1)
			exit()
if cnt:
	print(-1)
	exit()
print(ans)
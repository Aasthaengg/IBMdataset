k=int(input())
a=list(map(int,input().split()))
a.reverse()
ans1=2
ans2=2
for i in range(k):
	m,M=ans1,ans2
	ans1=((m-1)//a[i]+1)*a[i]
	ans2=M//a[i]*a[i]

	if ans1>ans2:
		print(-1)
		exit()

	ans1=ans1//a[i]*a[i]
	ans2=ans2//a[i]*a[i]+(a[i]-1)

if ans1>ans2:
	print(-1)
	exit()
else:
	print(ans1,ans2)
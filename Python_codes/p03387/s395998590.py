a=list(map(int,input().split()))
a.sort()
b=a[2]-a[1]
c=a[2]-a[0]
if (b+c)%2==0:
	print((b+c)//2)
else:
	print(((b+c)//2)+2)
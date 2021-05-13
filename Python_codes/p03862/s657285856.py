n , x= map(int , input().split())
arr = list(map(int , input().split()))
ans = []
tot=0
if arr[0]>x:
	tot = tot+(arr[0]-x)
	arr[0]=x
for i in range(1,n):
	if arr[i]+arr[i-1]>x:
		dif = ((arr[i]+arr[i-1])-x)
		tot = tot+dif
		if arr[i]-dif>=0:
			arr[i]=arr[i]-dif
		else:
			arr[i-1]=arr[i-1]-dif
print(tot)
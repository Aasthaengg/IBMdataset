k = int(input())
a = [int(i) for i in input().split()]
a,flag = a[::-1],True
if a[0]!=2: flag = False
else:
	x,y = 2,3
	for i in range(1,k):
		x2 = x-x%a[i]+min(x%a[i],1)*a[i]
		if x2>y:
			flag = False
			break
		else: x,y = x2,y-y%a[i]+a[i]-1
if flag: print(x,y)
else: print(-1)
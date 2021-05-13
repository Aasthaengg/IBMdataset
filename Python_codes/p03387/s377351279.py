a=list(map(int,input().split()))
a=sorted(a)
cnt=0
if a[0]==a[1] and a[1]==a[2]:
	print(0)
elif a[0]==a[1]:
	while True:
		a[0]+=1
		a[1]+=1
		cnt+=1
		if a[0]==a[2]:
			print(cnt)
			break
elif a[1]==a[2]:
	while True:
		a[0]+=2
		cnt+=1
		if a[0]==a[2]:
			print(cnt)
			break
		elif a[0]>a[2]:
			print(cnt+1)
			break
else:
	while True:
		a[0]+=1
		a[1]+=1
		cnt+=1
		if a[2]==a[1]:
			break
	while True:
		a[0]+=2
		cnt+=1
		if a[0]==a[2]:
			print(cnt)
			break
		elif a[0]>a[2]:
			print(cnt+1)
			break
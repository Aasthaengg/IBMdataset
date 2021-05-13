def resolve():
	n=int(input())
	a,b=map(int,input().split())
	p=list(map(int,input().split()))
	l=[0,0,0]
	for i in p:
		if i<=a:
			l[0]+=1
		elif i<=b:
			l[1]+=1
		else:
			l[2]+=1
	print(min(l))
resolve()
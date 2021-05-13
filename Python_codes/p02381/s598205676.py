while 1:
	n=float(input())
	if n==0:
		break
	l=list(map(float,input().split()))
	s=sum(l)
	a=s/n
	c=0
	for i in l:
		c+=((i-a)**2)
	import math
	print(math.sqrt(c/n))
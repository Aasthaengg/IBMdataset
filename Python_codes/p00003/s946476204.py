n=input()
for i in range(0,n):
	num=map(int, raw_input().split())
	num.sort()
	a=num[0]
	b=num[1]
	c=num[2]
	if c*c==a*a+b*b:
		print "YES"
	else:
		print "NO"
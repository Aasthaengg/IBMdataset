while True:
	a,b,c=map(str, input().split())
	if b=='?':
		break
	a=int(a)
	c=int(c)
	if b=='+':
		print(a+c)
	elif b=='*':
		print(a*c)
	elif b=='/':
		print(int(a/c))
	elif b=='-':
		print(a-c)
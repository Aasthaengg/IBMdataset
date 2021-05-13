a,b,c=map(int,input().split())
if b>=c:
	print(b+c)
else:
	if a+b>=c:
		print(c+b)
	else:
		print(b+a+b+1)
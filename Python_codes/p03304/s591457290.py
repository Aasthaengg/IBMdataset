n,m,d = map(int,input().split())
if n > d:
	if d == 0:
		print((m-1)*(1/n))
	else:
		print((m-1)*((1+(n-2*d)/n)/n))
else:
	print('0')
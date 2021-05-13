a,b,c,d = map(int,input().split())
e=(a+d-1)//d
f=(c+b-1)//b
if e>=f:
	print('Yes')
else:
	print('No')
a,b = map(int,input().split())

if a > b:
	print(a + max(a-1,b))
elif b > a:
	print(b + max(b-1,a))
else:
	print(a+b)

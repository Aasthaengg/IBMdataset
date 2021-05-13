a,b,c=map(int,input().split())
if a<b<c:
	print(a+b)
elif a<c<b:
	print(a+c)
elif b<a<c:
	print(b+a)
elif b<c<a:
	print(b+c)
elif c<a<b:
	print(c+a)
else:
	print(c+b)
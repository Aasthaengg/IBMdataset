a,b=map(int,input().split())
if len(str(a))>1 or len(str(b))>1:
	print("-1")
else:
	print(a*b)
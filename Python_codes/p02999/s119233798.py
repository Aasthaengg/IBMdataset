def rounding(x,a):
	if x<a:
		return 0
	else:
		return 10    

x,a = map(int,input().split())
print(rounding(x,a))
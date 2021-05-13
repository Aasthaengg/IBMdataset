a,b=map(int,input().split())
if a<=b:
	print(int(a*(10**(b)-1)/9))
else:
	print(int(b*(10**(a)-1)/9))
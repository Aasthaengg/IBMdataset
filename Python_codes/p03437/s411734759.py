b=[]
b = input().strip().split()
b[0]=int(b[0])
b[1]=int(b[1])
if b[0]%b[1]==0:
	print("-1")
else:
	print(b[0])

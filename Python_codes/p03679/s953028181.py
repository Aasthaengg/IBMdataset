x,a,b =map(int,input().split())
s = a-b
if s>=0:
	print("delicious")
elif s<0 and (x+s)>=0:
	print("safe")
else:
	print("dangerous")

a,b = list(map(int,input().split()))

x = (a+b)/2

if x != int(x):
	print(int(x) + 1)
else:
	print(int(x))
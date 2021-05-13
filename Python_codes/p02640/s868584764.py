X, Y = map(int, input().split())
if Y%2!=0 or Y<(X*2) or Y>(X*4):
	print("No")
else:
	print("Yes")
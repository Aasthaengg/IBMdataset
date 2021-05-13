a,b,c = [eval(x) for x in input().split()]
if a < b and b < c:
	print("Yes")
else:
	print("No")
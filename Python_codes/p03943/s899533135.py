a,b,c = [int(i) for i in input().split()]

if c == a + b or b == a + c or a == b + c:
	print("Yes")
else:
	print("No")
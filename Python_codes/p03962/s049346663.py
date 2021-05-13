a, b, c = [int(i) for i in input().split()]
if a == b == c:
	print(1)
elif a == b or a == c or b == c:
	print(2)
else:
	print(3)
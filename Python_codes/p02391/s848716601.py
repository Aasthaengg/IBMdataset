z = input()
x, y = tuple(z.split())
x = int(x)
y = int(y)

if x < y:
	print("a < b")
elif x > y:
	print("a > b")
else:
	print("a == b")
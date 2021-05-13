x = input()
a, b, c = tuple(x.split())
a = int(a)
b = int(b)
c = int(c)

if a < b and b < c:
	print("Yes")
else:
	print("No")
x, a, b = input().split()
x = int(x)
a = int(a)
b = int(b)

x_a = (x - a) ** 2
x_b = (x - b) ** 2
	


if x_a > x_b:
	print("B")

else:
	print("A")
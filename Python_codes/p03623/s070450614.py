x, a, b = input().split()
x = int(x)
a = int(a)
b = int(b)

if x > a:
	x_a = x - a
else:
	x_a = a - x

if x > b:
	x_b = x - b
else:
	x_b = b - x
	
if x_a > x_b:
	print("B")
else:
	print("A")

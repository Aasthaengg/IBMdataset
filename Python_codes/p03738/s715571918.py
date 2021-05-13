a = input()
b = input()
if a == b:
	print("EQUAL")
elif len(a) < len(b):
	print("LESS")
elif len(a) > len(b):
	print("GREATER")
elif a < b:
	print("LESS")
else:
	print("GREATER")
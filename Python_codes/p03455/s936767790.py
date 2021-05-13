a, b = [int(i) for i in input().split(" ")]
if (a % 2 == 0) | (b % 2 == 0):
	print("Even")
elif (a % 2 != 0) & (b % 2 != 0):
	print("Odd")
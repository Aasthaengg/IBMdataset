import math

number = int(input().replace(" " , ""))

sqrt = int(math.sqrt(number))

if sqrt * sqrt == number:
	print("Yes")
else:
	print("No")
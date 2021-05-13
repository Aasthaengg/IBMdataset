number = input()
length = len(number)

while number != "0":
	i = 0
	sum = 0
	while i < length:
		sum += int(number[i])
		i += 1
	print(sum)
	number = input()
	length = len(number)

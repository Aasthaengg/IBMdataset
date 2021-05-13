n = input()

while n != "0":
	sum = 0
	for i in n:
		sum += int(i)
	print(sum)
	n = input()
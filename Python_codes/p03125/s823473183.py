numbers = [int(i) for i in input().split()]

if numbers[1]%numbers[0] == 0:
	print(numbers[1] + numbers[0])
else:
	print(numbers[1] - numbers[0])
umbers = []
n = raw_input()

numbers = n.split(" ")

for i in range(2):
	numbers[i] = int(numbers[i])

print numbers[0] * numbers[1], 2 * (numbers[0] + numbers[1])  
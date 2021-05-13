numbers = []
n = raw_input()
s = raw_input()
print s
numbers = s.split(" ")
for i in range(int(n)):
	numbers[i] = int(numbers[i])


for i in range(1, int(n)):
	v = numbers[i]
	j = i - 1
	while (j >= 0 and numbers[j] > v):
		numbers[j + 1] = numbers[j]
		j -= 1
	numbers[j + 1] = v
	print ' '.join([str(a) for a in numbers])
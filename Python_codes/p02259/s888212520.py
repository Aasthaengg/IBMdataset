numbers = []
n = int(raw_input())
s = raw_input()
count = 0

numbers = s.split(" ")
for i in range(int(n)):
	numbers[i] = int(numbers[i])

flag = 1
while flag:
	flag = 0
	for j in range(n - 1, 0, -1):
		if numbers[j] < numbers[j - 1]:
			numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
			flag = 1
			count += 1
print ' '.join([str(a) for a in numbers])
print count
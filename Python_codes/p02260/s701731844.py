
numbers = []
n = int(raw_input())
s = raw_input()
count = 0

numbers = s.split(" ")
for i in range(int(n)):
	numbers[i] = int(numbers[i])

for i in range(int(n)):
	minj = i
	for j in range (i, n):
		if numbers[j] < numbers[minj]:
			minj = j
	if i != minj:	
	    numbers[i], numbers[minj] = numbers[minj], numbers[i]
	    count += 1

print ' '.join([str(a) for a in numbers])
print count 
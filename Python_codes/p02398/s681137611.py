numbers = map(int, raw_input().split())
count = 0
i = numbers[0]
while i <= numbers[1]:
	a = numbers[2] % i
	i += 1
	if a == 0:
		count += 1

print count
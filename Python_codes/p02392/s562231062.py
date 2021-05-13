numbers = []
n = raw_input()
numbers = n.split(" ")
for i in range(3):
	numbers[i] = int(numbers[i])

if numbers[0] < numbers[1] < numbers[2]:
	print "Yes"
else:
	print "No"
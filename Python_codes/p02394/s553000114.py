numbers = []
n = raw_input()
numbers = n.split(" ")
for i in range(5):
	numbers[i] = int(numbers[i])
W = numbers[0]
H = numbers[1]
x = numbers[2]
y = numbers[3]
r = numbers[4]

if x - r >= 0 and y - r >= 0 and x + r <= W and y + r <= H:
	print "Yes"
else:
	print "No"
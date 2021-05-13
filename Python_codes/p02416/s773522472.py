import sys

def sum_of_digits(x):
	sum = 0
	while x > 0:
		sum += x % 10
		x = x // 10

	return sum

#fin = open("test.txt", "r")
fin = sys.stdin

while True:
	x = int(fin.readline())

	if x == 0:
		break

	print(sum_of_digits(x))
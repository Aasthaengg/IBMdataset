import sys

#fin = open("test.txt", "r")
fin = sys.stdin

[r, c] = list(map(int, fin.readline().split()))

sum_col = [0 for i in range(c + 1)]

for i in range(r):
	input_list = list(map(int, fin.readline().split()))
	for j in range(c):
		sum_col[j] += input_list[j]
		print(input_list[j], end = " ")


	s = sum(input_list)

	sum_col[c] += s
	print(s)

for i in range(c):
	print(sum_col[i], end = " ")

print(sum_col[c])
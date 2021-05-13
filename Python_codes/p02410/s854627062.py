n, m = map(int, input().split()) # n = 3, m = 4
a_matrix = [list(map(int, input().split())) for row in range(n)] # [[1, 2, 0, 1], [0, 3, 0, 1], [4, 1, 1, 0]]
b_matrix = [int(input()) for row in range(m)] # [1, 2, 3, 0]

for i in range(n):
	combined = [a * b for (a, b) in zip(a_matrix[i], b_matrix)]
	result = 0
	for x in combined:
		result += x
	print(result)
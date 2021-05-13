import sys
import itertools

def can_be_composed(n, min_list, max_list, m, A):
	for i in range(1, n + 1):
		if m < min_list[i - 1]:
			continue
		if m > max_list[i - 1]:
			continue

		combination_list = list(itertools.combinations(A, i))
		for l in combination_list:
			if m == sum(l):
				return True

	return False

#fin = open("test.txt", "r")
fin = sys.stdin

n = int(fin.readline())
A = list(map(int, fin.readline().split()))
A.sort()
q = int(fin.readline())
m_list = list(map(int, fin.readline().split()))

min_list = [0]
min_list[0] += A[0]
for i in range(1, n):
	min_list.append(min_list[i - 1] + A[i])

max_list = [0]
max_list[0] += A[n - 1]
for i in range(1, n):
	max_list.append(max_list[i - 1] + A[n - i - 1])

for m in m_list:
	if can_be_composed(n, min_list, max_list, m, A):
		print("yes")
	else:
		print("no")
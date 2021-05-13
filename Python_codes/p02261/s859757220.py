def bubble_sort(A, n):
	for i in range(n):
		for j in range(n-1, i, -1):
			if A[j][1] < A[j-1][1]:
				A[j], A[j-1] = A[j-1], A[j]

	print(' '.join(A))

def selection_sort(A, n):
	for i in range(n):
		minj = i
		for j in range(i, n):
			if A[j][1] < A[minj][1]:
				minj = j
		if i != minj:
			A[i], A[minj] = A[minj], A[i]

	print(' '.join(A))

if __name__ == '__main__':
	n = int(input())
	A = list(input().split())
	B = A[:]

	bubble_sort(A, n)
	print('Stable')

	selection_sort(B, n)
	print('Stable' if A == B else 'Not stable')
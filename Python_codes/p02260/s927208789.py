# coding: utf-8

def selectionSort(A, N):
	A = A[:]
	count = 0
	for i in xrange(N):
		minj = i
		for j in xrange(i, N):
			if A[j] < A[minj]:
				minj = j
		if minj != i:
			A[i], A[minj] = A[minj], A[i]
			count += 1
	return A, count

def main():
	N = input()
	A = map(int, raw_input().split())
	sorted_, count = selectionSort(A, N)
	print ' '.join(map(str, sorted_))
	print count

if __name__ == '__main__':
	main()
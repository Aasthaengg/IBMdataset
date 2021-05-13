def InsertionSort(A , N):
	for i in range(1,N):
		v =  A[i]
		j = i -1 
		while j > -1 and A[j] > v:
			A[j+1] = A[j]
			j = j -1
		A[j+1] = v 
		print " ".join(map(str, A))

def main():
	N = int( raw_input() )
	A = map(int, raw_input().split())
	print " ".join(map(str, A))
	InsertionSort(A, N)

if __name__=='__main__':
	main()
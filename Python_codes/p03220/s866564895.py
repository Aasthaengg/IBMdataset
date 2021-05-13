if __name__ == '__main__':
	n = int(input())
	t,a = map(int,input().split())
	H = list(map(int,input().split()))

	A = [t - x * 0.006 for x in H]

	tmp = abs(a - A[0])
	ind = 0
	for i,y in enumerate(A,1):
		if tmp >= abs(a - y):
			tmp = abs(a - y)
			ind = i
		
	print(ind)

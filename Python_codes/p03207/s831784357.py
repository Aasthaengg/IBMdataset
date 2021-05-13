if __name__ == '__main__':

	n = int(input())
	
	A = []
	max_num = 0
	for i in range(n):
		cmd = int(input())
		max_num = max(max_num,cmd)
		A.append(cmd)

	ind = A.index(max_num)
	A[ind] = A[ind] // 2
	
	print(sum(A))

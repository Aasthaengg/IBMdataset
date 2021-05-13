if __name__ == '__main__':

	n = int(input())

	A = []
	for i in range(n):
		cmd = input().split()
		A.append([i+1,cmd[0],int(cmd[1])])

	B = sorted(A,key=lambda x:(x[1],-x[2]))
	for j in B:
		print(j[0])

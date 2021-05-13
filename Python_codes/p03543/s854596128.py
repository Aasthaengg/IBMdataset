if __name__ == '__main__':

	A = list(map(int,input()))

	if A[0]==A[1] and A[1]==A[2] and A[0]==A[2]:
		print("Yes")
	elif A[1]==A[2] and A[2]==A[3] and A[1]==A[3]:
		print("Yes")
	else:
		print("No")
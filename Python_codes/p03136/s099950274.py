if __name__ == '__main__':

	n = int(input())
	A = list(map(int,input().split()))

	max_n = max(A)

	if max_n < sum(A) - max_n:
		print("Yes")
	else:
		print("No")
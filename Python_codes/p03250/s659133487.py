if __name__ == '__main__':
	A = list(map(int,input().split()))
	B = sorted(A,reverse=True)

	ans = B[0] * 10 + B[1] + B[2]
	print(ans)

if __name__ == '__main__':

	n,k = map(int,input().split())

	A = []
	for i in range(n):
		cmd = int(input())
		A.append(cmd)

	B = sorted(A,reverse=True)

	ans = 10**9
	for j in range(n-k+1):
		tmp = B[j] - B[j+k-1]
		ans = min(ans,tmp)
	print(ans)
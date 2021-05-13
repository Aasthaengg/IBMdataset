def getlist():
	return list(map(int, input().split()))

con = 10 ** 9 + 7

#処理内容
def main():
	L = list(input())
	L = L[::-1]
	N = len(L)
	#前処理
	DP1 = [0] * (N + 1)
	DP2 = [0] * (N + 1)
	DP2[0] = 3
	for i in range(1, N + 1):
		DP2[i] = (3 * DP2[i - 1]) % con
	if L[0] == "1":
		DP1[0] = 3
	else:
		DP1[0] = 1

	#DP
	for i in range(1, N):
		if L[i] == "1":
			DP1[i] = (DP1[i - 1] * 2 + DP2[i - 1]) % con
		else:
			DP1[i] = DP1[i - 1]
	print(DP1[N - 1])


if __name__ == '__main__':
	main()
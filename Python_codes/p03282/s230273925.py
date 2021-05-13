if __name__ == '__main__':

	S = input()
	n = int(input())

	flg = False
	for x in range(n):
		if S[x] != "1":
			print(S[x])
			flg = True
			break
	if flg == False:
		print("1")
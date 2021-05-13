if __name__ == '__main__':
	S = input()
	s_len = len(S)

	tmp = 753-int(S[0])
	for x in range(s_len):
		if x+3 <= s_len:
			tmp = min(tmp,abs(753 - int(S[x:x+3])))
	print(tmp)

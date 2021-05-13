if __name__ == '__main__':
	S = input()
	T = input()

	set_S = set(S)
	set_T = set(T)
	if len(set_S) != len(set_T):
		print("No")
		exit()

	dic = dict()

	flg = True
	for x,y in zip(S,T):
		if x not in dic:
			dic[x] = y
		else:
			if dic[x] != y:
				flg = False
				break
	
	if flg :
		print("Yes")
	else:
		print("No")
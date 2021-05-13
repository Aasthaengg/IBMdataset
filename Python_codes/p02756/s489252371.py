if __name__ == '__main__':

	s = input()
	n = int(input())

	rvcnt = 0

	tmp = "S"
	tmp_before = ""
	tmp_after = ""
	
	for _ in range(n):
		q = input()
		if len(q) == 1:
			rvcnt += 1
		else:
			i,f,c = map(str,q.split())
			if f == "1":#先頭に追加
				if rvcnt % 2 == 0:
					#先頭に追加
					tmp_before = c + tmp_before
				else:
					#末尾に追加
					tmp_after = tmp_after + c
			else:#末尾に追加
				if rvcnt % 2 == 0:
					#末尾に追加
					tmp_after = tmp_after + c
				else:
					#先頭に追加
					tmp_before = c + tmp_before


	#仮想を元に戻す
	tmp1 = tmp.replace("S",s)
	#連結
	tmp2 = tmp_before + tmp1 + tmp_after

	#最後に反転するかを決定
	if rvcnt % 2 == 1:
		print(tmp2[::-1])
	else:
		print(tmp2)

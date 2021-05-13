
line,col = map(int,input().split(" "))

list_col = [0 for i in range(col+1)]
for _ in range(line):
	#行ループ
	data = list(map(int,input().split(" ")))
	data.append(sum(data))

	str_data = list(map(str,data))
	print(" ".join(str_data))

	#列ループ
	for j in range(col+1):
		list_col[j] += data[j]

str_col = list(map(str,list_col))
print(" ".join(str_col))



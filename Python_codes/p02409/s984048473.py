def create_List():
	re_list = [[],[],[],[]]
	for i in range(4):
		for j in range(3):
			re_list[i].append([0 for k in range(10)])
	return re_list

# ????????§??¨?????????????????§????????¨????????????(??????)
num = create_List()
for _ in range(int(input())):
	data = list(map(int,input().split()))
	num[data[0]-1][data[1]-1][data[2]-1] += data[3]

# ????????????
for i in range(4):
	for j in range(3):
		print(' ' + ' '.join(map(str,num[i][j])))
	if i == 3:
		break
	print('#'*20)
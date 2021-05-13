S = input()
flag = 0
for i in range(len(S)):
	if i%2 == 0 and S[i] != 'h':
		flag = 1
	if i%2 == 1 and S[i] != 'i':
		flag = 1
if flag == 1 or len(S)%2 == 1:
	print('No')
else:
	print('Yes')
n = int(input())
lst = []
for i in range(n):
	lst.append(list(map(int,input().split())))

cnt = 0

for i in range(n):
	if lst[i][0]==lst[i][1]:
		cnt += 1
	else:
		cnt = 0
	if cnt == 3:
		print('Yes')
		exit()
print('No')
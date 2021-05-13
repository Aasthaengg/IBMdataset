N,M = map(int,input().split())
target = list()
for i in range(N):
	target_list = list(map(int,input().split()))
	target_list.pop(0)
	target.append(target_list)

# print(target)

ans = dict()
for i in range(0,len(target)):
	for j in range(len(target[i])):
		if i == 0:
			ans[target[i][j]] = 1
		else:
			if target[i][j] in ans:
				ans[target[i][j]] += 1

ans_num = 0
for k in ans.keys():
	if ans[k] == N:
		ans_num += 1
print(ans_num)

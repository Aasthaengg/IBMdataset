import copy
import sys

array_data = map(int, raw_input().split())
r = array_data[0]
c = array_data[1]

array = []
for i in range(r):
	partial_array = map(int, raw_input().split())
	array.append(partial_array)

ans = copy.deepcopy(array)
for i in range(r):
	ans[i].append(sum(array[i]))
ans.append([])
for j in range(c+1):
	wa = 0
	for i in range(r):
		wa += ans[i][j]
	ans[r].append(wa)

for i in range(len(ans)):
	for j in range(len(ans[i])):
		if j != len(ans[i])-1:
			sys.stdout.write("{:} ".format(ans[i][j]))
		else:
			print(ans[i][j])
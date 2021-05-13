all_N = []
while True:
	N = list(map(int, input().split(' ')))
	if N[0] == 0 and N[0] == 0:
		break
	all_N.append(N)

for i in range(len(all_N)):
	for j in range(all_N[i][0]):
		print('#' * all_N[i][1])
	print('')
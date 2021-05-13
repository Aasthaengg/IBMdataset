N = int(input())
D = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N-2):
	if all(D[j][0] == D[j][1] for j in range(i, i+3)):
		print('Yes')
		break
else:
	print('No')

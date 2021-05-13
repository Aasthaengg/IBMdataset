H, W, A, B = map(int, input().split())
ans = [[0] * W for i in range(H)]
for i in range(A):
	for j in range(B):
		ans[j][i] = 1
i = A
while i < W:
	j = B
	while j < H:
		ans[j][i] = 1
		j += 1
	i += 1
for i in ans:
	for j in i:
		print(j, end='')
	print()
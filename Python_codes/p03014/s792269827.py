H, W = map(int, input().split())
S = [input() for _ in range(H)]

Left  = [[0] * 2100 for _ in range(2100)]
Right = [[0] * 2100 for _ in range(2100)]
Up    = [[0] * 2100 for _ in range(2100)]
Down  = [[0] * 2100 for _ in range(2100)]

for i in range(H):
	cur = 0
	for j in range(W):
		if S[i][j] == '#':
			cur = 0
		else:
			cur += 1
		Left[i][j] = cur

for i in range(H):
	cur = 0
	for j in range(W-1, -1, -1):
		if S[i][j] == '#':
			cur = 0
		else:
			cur += 1
		Right[i][j] = cur

for j in range(W):
	cur = 0
	for i in range(H):
		if S[i][j] == '#':
			cur = 0
		else:
			cur += 1
		Up[i][j] = cur

for j in range(W):
	cur = 0
	for i in range(H-1, -1, -1):
		if S[i][j] == '#':
			cur = 0
		else:
			cur += 1
		Down[i][j] = cur

cnt = 0
for i in range(H):
	for j in range(W):
		if S[i][j] == '#':
			continue
		cnt = max(cnt, Left[i][j] + Right[i][j] + Up[i][j] + Down[i][j] - 3)

print(cnt)
H,W = map(int, input().split())
grid = [-1] * (W+4) * 2
black_ind = []
for _ in range(H):
	grid += [-1]*2
	I = input()
	for i in range(W):
		if I[i] == '#':
			grid.append(1)
			black_ind.append(len(grid)-1)
		else:
			grid.append(0)
	grid += [-1]*2

grid += [-1] * (W+4) * 2

move = [1,-1,W+4,-(W+4)]
ans = 0
for b in black_ind:
	if grid[b] == 2:
		continue
	cnt_b = 1
	cnt_w = 0
	q = [b]
	grid[b] = 2
	while q:
		cp = q.pop()
		if grid[cp] == 2:
			for d in move:
				if grid[cp+d] == 0:
					grid[cp+d] = 3
					cnt_w += 1
					q.append(cp+d)
		elif grid[cp] == 3:
			for d in move:
				if grid[cp+d] == 1:
					grid[cp+d] = 2
					cnt_b += 1
					q.append(cp+d)

	ans += cnt_b * cnt_w
print(ans)


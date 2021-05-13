H, W, k = map(int, input().split())
s = [input() for _ in range(H)]
ans = []
vacant = 0
cnt = 0
for h in range(H):
	if s[h] == "."*W:
		vacant += 1
		continue
	else:
		cnt += 1
		tmp = []
		yet = False
		for w in range(W):
			if s[h][w] == "#":
				if not yet:
					yet = True
				else:
					cnt += 1
			tmp.append(cnt)

		for _ in range(vacant+1):
			ans.append(tmp)
		vacant = 0

for _ in range(vacant):
	ans.append(ans[-1])

for a in ans:
	print(*a, sep=" ")
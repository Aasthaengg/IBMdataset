m, k = map(int, input().split())
if k >= 2 ** m:
	print("-1")
elif k == 0:
	res = []
	for i in range(2 ** m):
		res += [i, i]
	print(" ".join(map(str, res)))
elif m == 0:
	print("0 0")
elif m == 1:
	if k == 0:
		print("0 0 1 1")
	else:
		print(-1)
else:
	used = set()
	pair = []
	for i in range(2 ** m):
		if i not in used:
			used.add(i)
			used.add(i ^ k)
			pair.append((i, i ^ k))
	res = []
	for i in range(0, len(pair), 2):
		res += [pair[i][0], pair[i][1], pair[i + 1][0], pair[i + 1][1],
				pair[i][1], pair[i][0], pair[i + 1][1], pair[i + 1][0]]
	print(" ".join(map(str, res)))
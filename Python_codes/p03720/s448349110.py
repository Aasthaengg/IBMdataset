n, m = map(int, input().split())
pairs = []
res = []
for _ in range(m):
	pair = list(map(int, input().split()))
	pairs.append(pair)
for i in range(1, n+1):
	c = 0
	for j in pairs:
		if i in j:
			c += 1
	res.append(c)
for i in res:
	print(i)
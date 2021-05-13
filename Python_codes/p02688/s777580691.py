def line():
	return [int(i) for i in input().split(" ")]
n, k = line()
vis = [0 for i in range(n)]
for _ in range(k):
	line()
	for i in line():
		vis[i-1] = 1
print(vis.count(0))

n = int(input())
for _ in range(n):
	edges = list(map(int, input().split()))
	if len(edges) == 0:
		break
	edges.sort()

	if edges[0] ** 2 + edges[1] ** 2 == edges[2] ** 2:
		print("YES")
	else:
		print("NO")
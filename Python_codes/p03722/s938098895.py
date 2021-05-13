n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]


def bellman_ford(s, g):
	# loop 0 - (n-1) : bellman ford
	# loop n - (2n-1): check g can be updated
	dist = [float("inf")] * n
	dist[s] = 0
	for i in range(2 * n):
		for a, b, c in abc:
			a -= 1
			b -= 1
			c = -c

			if dist[b] > dist[a] + c:
				dist[b] = dist[a] + c
				if i >= n:
					dist[b] = -float("inf")

	if dist[g] == -float("inf"):
		ret = "inf"

	else:
		ret = -dist[g]

	return ret


ans = bellman_ford(0, n - 1)
print(ans)

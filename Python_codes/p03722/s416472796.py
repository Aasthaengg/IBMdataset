def reachable(es, source):
	ret = {source}
	Q = [source]
	while Q:
		cur = Q.pop()
		for nxt in es[cur]:
			if nxt not in ret:
				Q.append(nxt)
				ret.add(nxt)
	return ret

def BellmanFord(V: int, es: list, source=0):
	INF = float("inf")
	D = [INF] * V
	D[source] = 0
	for _ in range(V):
		upd = False
		for f, t, c in es:
			tmp = D[f] + c
			if D[t] > tmp:
				D[t] = tmp
				upd = True
		if not upd:
			return D[-1]
	else:
		# Negative Cycle
		return None


def main():
	N, M, *L = map(int, open(0).read().split())
	fwd = [[] for _ in range(N)]
	bwd = [[] for _ in range(N)]
	tmp = []
	for a, b, c in zip(*[iter(L)] * 3):
		fwd[a - 1].append(b - 1)
		bwd[b - 1].append(a - 1)
		tmp += [(a - 1, b - 1, - c)]
	ra = reachable(fwd, 0) & reachable(bwd, N - 1)
	ans = BellmanFord(N, [(a, b, c) for a, b, c in tmp if a in ra and b in ra])
	if ans == None:
		print("inf")
	else:
		print(-ans)


if __name__ == "__main__":
	main()
n, m, *L = map(int, open(0).read().split())
con = [[] for _ in range(n)]
vis = [None] * n
for l, r, d in zip(*[iter(L)] * 3):
	con[l - 1] += [(r - 1, d)]
	con[r - 1] += [(l - 1, -d)]

def check(s):
	if vis[s] is not None:
		return True
	q = [s]
	vis[s] = 0
	while q:
		cur = q.pop()
		for nxt, d in con[cur]:
			if vis[nxt] is not None:
				if vis[nxt] != vis[cur] + d:
					return False
				continue
			vis[nxt] = vis[cur] + d
			q += [nxt]
	return True

print("Yes" if all(check(s) for s in range(n)) else "No")
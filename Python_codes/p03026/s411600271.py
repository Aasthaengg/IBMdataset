n, *L = map(int, open(0).read().split())
ab = L[:2 * n - 2]
c = sorted(L[2 * n - 2:])
con = [[] for _ in range(n)]
ans = [0] * n
tot = sum(c) - max(c)
for a, b in zip(*[iter(ab)] * 2):
	con[a - 1].append(b - 1)
	con[b - 1].append(a - 1)
vis = [0] * n
q = [0]
vis[0] = 1
while q:
	cur = q.pop()
	ans[cur] = c.pop()
	for nxt in con[cur]:
		if vis[nxt]:
			continue
		q.append(nxt)
		vis[nxt] = 1
print(tot)
print(*ans)

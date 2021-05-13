def prepare(m, mod=10 ** 9 + 7):
	fac = [1] * (m + 1)
	inv = [1] * (m + 1)
	for i in range(1, m + 1):
		fac[i] = fac[i - 1] * i % mod
	inv[-1] = pow(fac[-1], mod - 2, mod)
	for i in range(m - 1, -1, -1):
		inv[i] = inv[i + 1] * (i + 1) % mod
	return fac, inv

def main():
	n, k, *L = map(int, open(0).read().split())
	mod = 10 ** 9 + 7
	fac, inv = prepare(k)
	con = [[] for _ in range(n)]
	cnt = [0] * n
	vis = [False] * n
	for s, t in zip(*[iter(L)] * 2):
		con[s - 1] += [t - 1]
		con[t - 1] += [s - 1]
		cnt[s - 1] += 1
		cnt[t - 1] += 1
	if any(c + 1 > k for c in cnt):
		print(0)
		exit()
	q = [0]
	vis[0] = True
	ans = fac[k] * inv[k - cnt[0] - 1] % mod
	while q:
		cur = q.pop()
		for nxt in con[cur]:
			if vis[nxt]:
				continue
			ans *= fac[k - 2] * inv[k - cnt[nxt] - 1] % mod
			ans %= mod
			vis[nxt] = True
			q.append(nxt)
	print(ans)

if __name__ == "__main__":
	main()
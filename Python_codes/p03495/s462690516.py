from collections import Counter

def resolve():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	c = Counter(a)
	lc = len(c.keys())
	if lc > k:
		v = 0
		sc = sorted(c.values())
		for i in range(lc-k):
			v += sc[i]
		print(v)
	else:
		print(0)
resolve()
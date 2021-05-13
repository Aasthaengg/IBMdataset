import collections
s = list(raw_input())
r = 0
mod = 10 ** 9 + 7
h= collections.Counter()
h[0] += 1
for v in s:

	v = int(v) if v != '?' else v
	hh = collections.Counter()
	for u in range(13):
		if v != '?':
			hh[(u * 10 + v) % 13] += h[u]

		else:
			for vv in range(10):
				hh[(u * 10 + vv) % 13] += h[u]
	for k in hh:
		hh[k] %= mod
	h = hh
print h[5]
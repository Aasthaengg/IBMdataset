import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N = ri()
S = []
for i in range(N):
	S.append(rs())

import collections
h = collections.defaultdict(int)
for s in S:
	l = [0] * 26
	for c in s:
		n = ord(c)-ord('a')
		l[n] += 1
	h[tuple(l)] += 1

def comb(n, k):
	p, q = 1, 1
	for i in range(1, k+1):
		p = p * (n-i+1)
		q = q * i
	return p // q

ans = 0
for k, v in h.items():
	if v > 1:
		ans += comb(v, 2)
print(ans)

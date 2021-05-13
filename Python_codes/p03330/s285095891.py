import sys
input = sys.stdin.readline
from collections import Counter

n, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]
a = [list(map(int, input().split())) for _ in range(n)]
zer, one, two = Counter(), Counter(), Counter()
for i, l in enumerate(a):
	for j, x in enumerate(l):
		x -= 1
		if (i + j) % 3 == 0:
			zer[x] += 1
		elif (i + j) % 3 == 1:
			one[x] += 1
		else:
			two[x] += 1
ans = 1 << 30
for f in range(c):
	for s in range(c):
		if f == s:
			continue
		for t in range(c):
			if f == t or s == t:
				continue
			cand = sum(d[k][f] * v for k, v in zer.items()) + sum(d[k][s] * v for k, v in one.items()) + sum(d[k][t] * v for k, v in two.items())
			if ans > cand:
				ans = cand
print(ans)
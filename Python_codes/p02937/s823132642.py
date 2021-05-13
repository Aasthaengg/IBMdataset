import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

s = rs()
t = rs()


import collections
pos = collections.defaultdict(list)
for i, c in enumerate(s):
	pos[c].append(i)

import bisect

num = 0
cur = -1

for c in t:
	if c not in pos:
		print(-1)
		exit()
	i = bisect.bisect_right(pos[c], cur)
	if i == len(pos[c]):
		i = 0
		num += 1
	cur = pos[c][i]
print(num*len(s)+cur+1)


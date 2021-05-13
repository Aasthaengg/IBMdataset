import itertools
import collections as c
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
vectors = []
for xy1,xy2 in itertools.combinations(XY,2):
	p = xy2[0] - xy1[0]
	q = xy2[1] - xy1[1]

	vectors.append((p,q))
	vectors.append((-p,-q))

V = c.Counter(vectors)
if N >= 2:
	x = max(V.values())
	ans = N-x
else:
	ans = 1

print(ans)
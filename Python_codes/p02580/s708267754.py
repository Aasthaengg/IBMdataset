import sys
input = sys.stdin.readline
H, W, M = map(int, input().split())


vert = [0] * (2*W)

def update(i, d):
	i += W
	vert[i] += d
	while i > 1:
		i >>= 1
		vert[i] = max(vert[i*2], vert[i*2+1])


lines = [[] for _ in range(H)]
for _ in range(M):
	y, x = map(lambda s: int(s)-1, input().split())
	lines[y].append(x)
	update(x, 1)

best = 0

for l in lines:
	for x in l: update(x, -1)
	best = max(best, len(l) + vert[1])
	for x in l: update(x, 1)

print(best)

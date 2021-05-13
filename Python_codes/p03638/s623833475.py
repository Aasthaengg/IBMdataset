
h, w= map(int, raw_input().split())
n = int(raw_input())
ais = map(int, raw_input().split())
mat = [[-1 for _ in range(w)] for ii in range(h)]
import collections
color = 0
vis = set([])
def bfs(start, color, count,mat):
	q = collections.deque([start])
	vis = set([start])
	while(q and count):
		count -=1
		cur = q.popleft()
		mat[cur[0]][cur[1]] = color + 1
		i,j = cur
		for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
			if 0 <= ni < len(mat) and 0<= nj < len(mat[0]):
				if (ni,nj) not in vis:
					vis.add((ni,nj))
					q.append((ni,nj))

for i in range(len(mat)):
	for j in range(len(mat[0]))[::(-1 if i % 2 else 1)]:
		mat[i][j] = color +1
		ais[color] -= 1
		if ais[color] == 0: color +=1
for l in mat:
	print ' '.join(map(str,l))
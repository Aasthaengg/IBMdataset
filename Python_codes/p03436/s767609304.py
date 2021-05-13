
import collections
h,p = map(int, raw_input().split())#10 37
mat = [list(raw_input()) for l in range(h)]
q = collections.deque([((0,0), 1)])

vis = set([(0,0)])
r  = float('inf')

while(q):
	u,d = q.popleft()

	if u == (h-1, p-1):
		r = d
		break
	for v in [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1),(u[0],u[1]-1)]:
		if 0 <= v[0] < len(mat) and 0 <= v[1] < len(mat[0]):
			if v not in vis and mat[v[0]][v[1]] == '.':
				vis.add(v)
				q.append((v, d+1))

cc = collections.Counter()
for l in mat:
	for e in l:
		cc[e]+=1

if r < float('inf'):
	print cc['.'] - r
else:
	print -1

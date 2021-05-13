import collections
def f(mat):
	q,vis = collections.deque([((0,0), 1)]), set([(0,0)])
	while(q):
		u,d = q.popleft()
		if u == (len(mat)-1, len(mat[0])-1): return collections.Counter(reduce(lambda x,y:x+y, mat))['.'] - d
		for v in [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1),(u[0],u[1]-1)]:
			if 0 <= v[0] < len(mat) and 0 <= v[1] < len(mat[0]) and (v not in vis) and mat[v[0]][v[1]] == '.':
				vis.add(v)
				q.append((v, d+1))
	return -1
print f([list(raw_input()) for l in range(map(int, raw_input().split())[0])])
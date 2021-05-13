import collections
h,w = map(int, raw_input().split())
mat = [map(int, raw_input().split(' ')) for _ in range(h)]
elems = [(i,j) for i in range(len(mat)) for j in range(len(mat[0]))]
elems.sort(key = lambda x: x[0] + x[1])
q = collections.deque(elems)
moves = []
while(q):
	i,j = q.popleft()
	if mat[i][j] % 2:
		if j + 1 < len(mat[0]):
			mat[i][j] -= 1
			mat[i][j+1] += 1
			moves.append([(i+1,j+1), (i+1, j + 2)])
			#q.append((i,j + 1))
		elif i + 1 < len(mat):
			mat[i][j] -=1
			mat[i+1][j] += 1
			moves.append([(i+1,j+1), (i+2, j+1)])
			#q.append((i + 1,j ))
print len(moves)
for u,v in moves: print u[0],u[1],v[0],v[1]
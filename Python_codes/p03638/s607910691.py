
import collections
h, w= map(int, raw_input().split())
n,ais = int(raw_input()), map(int, raw_input().split())
mat = [[-1 for _ in range(w)] for ii in range(h)]
c = 0
for i in range(len(mat)):
	for j in range(len(mat[0]))[::(-1 if i % 2 else 1)]:
		mat[i][j] = c +1
		ais[c] -= 1
		if ais[c] == 0: c +=1
for l in mat: print ' '.join(map(str,l))
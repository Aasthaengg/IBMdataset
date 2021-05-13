import collections
h,w,d = map(int, raw_input().split())
mat = [map(int, raw_input().split()) for i in range(h)]
coord,cost = {mat[i][j]:(i,j) for i in range(len(mat)) for j in range(len(mat[0]))}, collections.Counter()
def f(uu,vv): 
	return abs(uu[0] -vv[0]) + abs(uu[1] -vv[1]) 
for u in range(1, h * w + 1):
	if u - d >= 1: cost[u] = f(coord[u], coord[u - d]) + cost[u - d]
for qi in  range(int(raw_input())):
	u,v = map(int, raw_input().split())
	print cost[v] - cost[u]
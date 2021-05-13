H,w,d = map(int, raw_input().split())
mat = [map(int, raw_input().split()) for i in range(H)]

h = {}
cost = {}
for i in range(len(mat)):
	for j in range(len(mat[0])):
		h[mat[i][j]] = (i,j)

import collections
cost = collections.Counter()
def f(uu,vv): return abs(uu[0] -vv[0]) + abs(uu[1] -vv[1]) 
for u in range(1,H*w + 1):
	if u - d >= 1: cost[u] = f(h[u], h[u - d]) + cost[u - d]


def g(u,v, cost,d): return cost[v] - cost[u]# if  in cost else 0) 

for qi in  range(int(raw_input())):
	u,v = map(int, raw_input().split())
	print g(u,v,cost, d)
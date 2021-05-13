import sys
sys.setrecursionlimit(10**6)

import math

N=int(input())

G=[[] for i in range(N)]
for _ in range(N-1):
	a,b=map(lambda x:int(x)-1,input().split())
	G[a].append(b)
	G[b].append(a)

depth=[[0]*N for i in range(2)]

def dfs(d, i, p, k=0):
	for t in G[i]:
		if t!=p:
			depth[k][t]=d
			dfs(d+1, t, i,k)


dfs(1,0,-1, 0)
dfs(1,N-1,-1, 1)

cnt=0
for i,j in zip(depth[0], depth[1]):
	if i<=j:
		cnt+=1

print('Fennec' if cnt*2>N else 'Snuke')

import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
G = {}
for node in range(1,N+1):
	G[node] = set()
for _ in range(M):
	x,y = map(int,input().split())
	G[x].add(y)

maxpath = [-1 for _ in range(N+1)]

def maxpa(G,source,maxpath):
	if maxpath[source] != -1:
		return maxpath[source]
	else:	
		if len(G[source]) == 0:
			maxpath[source] = 0
			return maxpath[source]
		else:	
			for ngbr in G[source]:
				maxpath[source] = max(maxpath[source],1+maxpa(G,ngbr,maxpath))
			return maxpath[source]

for i in range(1,N+1):
	if maxpath[i]==-1:
		maxpa(G,i,maxpath)

print(max(maxpath))
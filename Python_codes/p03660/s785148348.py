from collections import*
N,*AB=map(int,open(0).read().split())
E=[[]for _ in range(N+1)]
for a,b in zip(*[iter(AB)]*2):
	E[a]+=[b]
	E[b]+=[a]
def g(s):
	Q=deque([s]);d=[0]*(N+1)
	while Q:
		v=Q.popleft()
		for u in E[v]:
			if d[u]==0:
				Q+=[u]
				d[u]=d[v]+1
	return d[1:]
print("SFneunknee c"[0<sum(1 if f<=s else-1 for f,s in zip(g(1),g(N)))::2])
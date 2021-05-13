from collections import deque
def F(m):
	q=deque([m])
	d=[-1]*n
	while q:
		cur=q.popleft()
		for nxt in G[cur]:
			if d[nxt]<0:
				q.append(nxt)
				d[nxt]=d[cur]+1
	return d
def solve():
	global n,G
	n,*L=map(int,open(0).read().split())
	G=[[]for _ in range(n)]
	for a,b in zip(*[iter(L)]*2):
		G[a-1]+=[b-1]
		G[b-1]+=[a-1]
	print("FSennunkeec"[sum(i>j or-1 for i,j in zip(F(0),F(n-1)))>=0::2])
if __name__=="__main__":solve()
from collections import deque
N,M,*L,S,T = map(int,open(0).read().split())
G = [[] for _ in range(N)]
step = [0 for _ in range(N)]
step[S-1] = 1
for u,v in zip(*[iter(L)]*2):
	G[u-1].append(v-1)
q = deque([(S-1,0)])
while q:
	cur,d = q.popleft()
	for nxt in G[cur]:
		if nxt==T-1 and (d+1)%3==0:
			print((d+1)//3)
			exit()
		if not step[nxt] & 1<<((d+1)%3):
			step[nxt] |= 1<<(d+1)%3
			q.append((nxt,d+1))
print(-1)
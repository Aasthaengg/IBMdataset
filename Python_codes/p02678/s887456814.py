from collections import deque

N,M=map(int,input().split())
m=[[] for _ in range(N)]
n=[-1]*N
n[0]=0
for _ in range(M):
	a,b=map(int,input().split())
	m[a-1].append(b-1)
	m[b-1].append(a-1)

def bfs():
	que=deque([])
	que.append(0)
	while que:
		p=que.popleft()
		for i in m[p]:
			if n[i]==-1:
				que.append(i)
				n[i]=p+1

bfs()

print('Yes')
for j in range(1,N):
	print(n[j])
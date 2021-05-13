from collections import deque

n,q = map(int,input().split())
queue = deque()
for i in range(n):
	name,time = input().split()
	queue.append((name, int(time)))

t = 0
while queue:
	name,time = queue.popleft()
	t += min(q, time)
	if time > q:
		queue.append((name, time-q))
	else:
		print(name,t)

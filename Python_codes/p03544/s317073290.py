import collections
n,q = int(raw_input()) + 1, collections.deque()
while(n):
	q.append(sum(list(q)) if len(q) == 2 else (2  - len(q)))
	if len(q) == 3: 
		q.popleft()

	n -=1
print q[-1]

import collections
n,k = map(int, raw_input().split(' '))
heights = [int(raw_input()) for _ in range(n)]
heights.sort()
q = collections.deque([])
r =  float('inf') 
for h in heights:
	q.append(h)
	if len(q) == k + 1: q.popleft()
	if k and len(q) == k:
		r =min(r, q[-1] - q[0])
print r if k else 0
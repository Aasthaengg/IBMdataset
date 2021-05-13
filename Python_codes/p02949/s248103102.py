import sys

n, m, p = map(int, sys.stdin.readline().split())

abc = []
# edge = [[] for _ in range(n)]
rev_edge = [[] for _ in range(n)]

for _ in range(m):
	a, b, c = map(int, sys.stdin.readline().split())
	abc.append((a-1, b-1, p-c))
	rev_edge[b-1].append(a-1)

def dfs(e, s):
	v_set = {s, }
	stack = [s]

	while stack:
		v = stack.pop()
		for next_v in e[v]:
			if not next_v in v_set:
				stack.append(next_v)
				v_set.add(next_v)
	return v_set

def bellman_ford(sub_abc, n):
	dist = [float('inf')]*n 
	dist[0] = 0

	for _ in range(n):
		updated = False
		for ele in sub_abc:
			a, b, d = ele
			if dist[a] + d < dist[b]:
				dist[b] = dist[a] + d 
				updated = True
		if not updated:
			break
	else:
		return -1

	return max(-dist[n-1], 0)

use = dfs(rev_edge, n-1)
print(bellman_ford([(a, b, c) for a, b, c in abc if a in use and b in use], n))
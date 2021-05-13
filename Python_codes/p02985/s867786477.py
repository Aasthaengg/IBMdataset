from collections import defaultdict

mod = pow(10, 9) + 7

n, k = map(int, input().split())

graph = defaultdict(list)

for _ in range(n-1):
	a, b = map(int, input().split())
	a -= 1
	b -= 1
	graph[a].append(b)
	graph[b].append(a)

def dfs(v):
	global graph, k
	ans = k	# k choices of color for root
	stack = [v]
	vis_set = {v, }

	while stack:
		v = stack.pop()
		if v==0: 
			avail_count = k-1
		else: 
			avail_count = k-2
		for nxt in graph[v]:
			if nxt not in vis_set:
				if avail_count <= 0:
					return 0
				ans = (ans*avail_count)%mod
				avail_count -= 1
				stack.append(nxt)
				vis_set.add(nxt)
	return ans

ans = dfs(0)
print(ans)
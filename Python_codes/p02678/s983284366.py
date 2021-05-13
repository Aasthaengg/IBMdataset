def main():
	
	from collections import deque
	n,m = map(int,input().split())
	l = [list(map(int, input().split())) for i in range(m)]
	graph = [[] for _ in range(n+1)]
	
	for i in range(m):
		a,b = l[i]
		graph[a].append(b)
		graph[b].append(a)

	dist = [-1] * (n+1)
	dist[0] = 0
	dist[1] = 0

	d = deque()
	d.append(1)

	while d:
		v = d.popleft()
		for i in graph[v]:
			if dist[i] != -1:
				continue
			dist[i] = dist[v] + 1
			d.append(i)

	if graph[1] == '':
		print("No")
	else:
		print("Yes")
		for i in range(2,n+1):
			if dist[i] == 1:
				print(1)
			else:
				for room in range(len(graph[i])):
					if dist[i]-1 == dist[graph[i][room]]:
						print(graph[i][room])
						break
	


if __name__ == '__main__':
	main()
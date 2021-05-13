import heapq
import sys


def dijkstra(n, paths, root):
	total_cost = [10 ** 9] * (n + 1)
	total_cost[root] = 0

	not_checked = set(range(1, n + 1))
	checked = set()
	cur_node = root
	h = []

	while not_checked:
		checked.add(cur_node)
		not_checked -= {cur_node}

		for next_node, cost in paths[cur_node]:
			if next_node in not_checked:
				heapq.heappush(h, (total_cost[cur_node] + cost, next_node))

		if not_checked:
			cost, next_node = heapq.heappop(h)

			while next_node in checked:
				cost, next_node = heapq.heappop(h)

			cur_node = next_node
			total_cost[cur_node] = cost

	return total_cost
		

def main():
	readline = sys.stdin.readline

	n = int(readline().rstrip())

	path = []
	for _ in range(n + 1):
		path.append([])

	for _ in range(n - 1):
		a, b, c = map(int, readline().rstrip().split())
		path[a].append((b, c))
		path[b].append((a, c))

	

	q, k = map(int, readline().rstrip().split())

	cost_from_k = dijkstra(n, path, k)

	for _ in range(q):
		x, y = map(int, readline().rstrip().split())
		print(cost_from_k[x] + cost_from_k[y])


if __name__ == '__main__':
	main()

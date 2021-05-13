from collections import defaultdict
import heapq


def dijkstra(N, start, adj_nodes, costs):
    INF = 10**15
    dist = [INF for _ in range(N)]
    dist[start] = 0
    frontier = [(0, start)]
    while len(frontier) > 0:
        d, node = heapq.heappop(frontier)
        for next_node in adj_nodes[node]:
            if dist[next_node] > d + costs[(node, next_node)]:
                dist[next_node] = d + costs[(node, next_node)]
                frontier.append((dist[next_node], next_node))
    return dist


def main():
    N = int(input())
    adj_nodes = defaultdict(list)
    costs = defaultdict(int)
    for _ in range(N - 1):
        a, b, c = list(map(int, input().split(' ')))
        a -= 1
        b -= 1
        adj_nodes[a].append(b)
        adj_nodes[b].append(a)
        costs[(a, b)] = c
        costs[(b, a)] = c
    Q, K = list(map(int, input().split(' ')))
    K -= 1
    queries = [list(map(lambda q: int(q) - 1, input().split(' '))) for _ in range(Q)]
    dist = dijkstra(N, K, adj_nodes, costs)
    for query in queries:
        x, y = query
        print(dist[x] + dist[y])


if __name__ == '__main__':
    main()
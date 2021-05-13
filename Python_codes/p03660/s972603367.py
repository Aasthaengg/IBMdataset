from collections import defaultdict
import heapq
INF = 10**6


def dijkstra(N, adj_nodes, start_node, non_use_node):
    assert start_node != non_use_node
    d = [INF for _ in range(N)]
    d[start_node] = 0
    frontier = [(0, start_node)]
    while len(frontier) > 0:
        dist, node = heapq.heappop(frontier)
        for next_node in adj_nodes[node]:
            if next_node == non_use_node:
                continue
            if d[next_node] > dist + 1:
                d[next_node] = dist + 1
                heapq.heappush(frontier, (d[next_node], next_node))
    return d


def main():
    N = int(input())
    adj_nodes = defaultdict(list)
    for _ in range(N - 1):
        a, b = list(map(int, input().split(' ')))
        a -= 1
        b -= 1
        adj_nodes[a].append(b)
        adj_nodes[b].append(a)
    fen_node, snu_node = 0, N - 1
    d_fen = dijkstra(N, adj_nodes, fen_node, snu_node)
    d_snu = dijkstra(N, adj_nodes, snu_node, fen_node)
    fen_score = 0
    for f, s in zip(d_fen, d_snu):
        fen_score += 1 if f <= s else 0
    snu_score = N - fen_score
    # answer
    if fen_score <= snu_score:
        print('Snuke')
    else:
        print('Fennec')


if __name__ == '__main__':
    main()
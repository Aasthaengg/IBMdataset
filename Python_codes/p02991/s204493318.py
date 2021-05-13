import collections
import queue
import sys

input = sys.stdin.readline


class AtCoder:
    def main(self):
        N, M = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(M)]
        S, T = map(int, input().split())

        edge_map = collections.defaultdict(list)
        for u, v in edges:
            edge_map[u - 1].append(v - 1)

        q = queue.Queue()
        q.put((S - 1, 0))

        INF = 10 ** 5
        dist = [[INF] * 3 for _ in range(N)]
        dist[S - 1][0] = 0
        while not q.empty():
            node, kkp = q.get()

            for next_node in edge_map[node]:
                next_kkp = (kkp + 1) % 3
                if dist[next_node][next_kkp] == INF:
                    dist[next_node][next_kkp] = dist[node][kkp] + 1
                    q.put((next_node, next_kkp))

        if dist[T - 1][0] == INF:
            print(-1)
        else:
            print(dist[T - 1][0] // 3)


# Run main
if __name__ == '__main__':
    AtCoder().main()
